struct thread
{
	// ....
	int priority;			   /* Priority. */

	int init_priority;           // 스레드의 원래 우선순위 저장
	struct list donations;           // 이 스레드에게 우선순위를 기부한 스레드들의 리스트
	struct list_elem donation_elem;  // donations 리스트에 사용될 리스트 요소
	struct lock *wait_on_lock;    // 스레드가 현재 대기 중인 lock의 주소
	// ....
}
/*우선순위를 고려한 Lock, Semaphore, Condition Variable 구현을 위해 새로운 변수들 선언*/
static void
init_thread (struct thread *t, const char *name, int priority) {
	ASSERT (t != NULL);
	ASSERT (PRI_MIN <= priority && priority <= PRI_MAX);
	ASSERT (name != NULL);

	memset (t, 0, sizeof *t);
	t->status = THREAD_BLOCKED;
	strlcpy (t->name, name, sizeof t->name);
	t->tf.rsp = (uint64_t) t + PGSIZE - sizeof (void *);
	t->priority = priority;             
	
	// 구조체에 새로 선언한 변수들 초기화
  t->init_priority = priority;
  t->wait_on_lock = NULL;
  list_init (&t->donations);
	
	t->magic = THREAD_MAGIC;
}
/*
donations 리스트를 우선순위 기준으로 정렬하기 위해 list_insert_ordered에 인자로 쓰일 함수 정의
*/
bool
thread_compare_donate_priority (const struct list_elem *l, 
				const struct list_elem *s, void *aux UNUSED)
{
	return list_entry (l, struct thread, donation_elem)->priority
		 > list_entry (s, struct thread, donation_elem)->priority;
}
/*
- Multiple Donation을 고려하여 depth를 임의로 8로 설정(성능을 더 높이고 싶다면 더 높은 숫자로 설정, 시간을 좀 더 빠르게 하고 싶다면 낮은 숫자로 설정), 재귀 형식으로 반복
- 이로 인하여 lock의 holder가 필요로 하는 lock(lock→holder→wait_on_lock)을 타고 올라가며 그중 가장 높은 우선순위를 가지는 스레드를 찾고 우선 순위를 비교하여 상속 받을 수 있음
- 재귀를 풀어 쓴다면**lock→holder→wait_on_lock→holder→wait_on_lock→holder→wait_on_lock**와 같이 표현 가능하며 해당 과정을 8번 반복하며 donations 리스트의 스레드들을 살펴보며 상속 관계를 정리하도록 구현
*/
void
donate_priority (void)
{
  int depth;
  struct thread *cur = thread_current ();

  for (depth = 0; depth < 8; depth++){
    if (!cur->wait_on_lock) break;
      struct thread *holder = cur->wait_on_lock->holder;
      holder->priority = cur->priority;
      cur = holder;
  }
}
/*우선순위를 고려하여 waiters 리스트가 정렬되도록 구현*/
void
sema_down (struct semaphore *sema) {
	enum intr_level old_level;

	ASSERT (sema != NULL);
	ASSERT (!intr_context ());

	old_level = intr_disable ();
	while (sema->value == 0) {
		list_insert_ordered(&sema->waiters, &thread_current ()->elem, thread_priority_compare, NULL);
		thread_block ();
	}
	sema->value--;
	intr_set_level (old_level);
}
/*
- 현재 실행중인 스레드가 매개변수 lock을 얻도록 하는 함수
- **lock->holder**가 존재하는 경우 해당 lock은 다른 스레드가 실행 되어야 사용 가능함을 알 수 있음
- **lock->holder**가 존재하는 경우 현재 실행중인 스레드의 **wait_on_lock**에 ****lock을 등록함
- lock→holder 스레드의 **donations에** 현재 실행중인 스레드를 추가하고 정렬(우선순위 높은 스레드가 **donations** 리스트 앞쪽에 오도록)
- **donate_priority** 함수를 이용하여 lock→holder의 우선순위(priority)보다 **donations** 리스트에 있는 스레드의 priority가 높은 경우 lock→holder가 해당 우선 순위를 상속받도록 구현
- 현재 실행중인 스레드가 lock을 받게 되면(lock의 holder가 현재 스레드가 된다면) 현재 스레드의 **wait_on_lock**을 NULL로 변경
*/
void
lock_acquire (struct lock *lock) {
	ASSERT (lock != NULL);
	ASSERT (!intr_context ());
	ASSERT (!lock_held_by_current_thread (lock));

	struct thread *cur = thread_current ();
	if (lock->holder) {
		cur->wait_on_lock = lock;
		list_insert_ordered (&lock->holder->donations, &cur->donation_elem, 
					thread_compare_donate_priority, 0);
		donate_priority ();
	}

	sema_down (&lock->semaphore);
	
	cur->wait_on_lock = NULL;
	
	lock->holder = cur;
}

/*
- 매개변수로 받는 lock의 정보를 제거하기 위한 함수
- 현재 실행중인 스레드의 donations 리스트 안에 있는 스레드들을 반복문으로 확인하며 wait_on_lock의 값으로 lock을 가지는 스레드가 존재하는 경우 donations 리스트에서 제거
- lock을 제거했기 때문에 기다릴 필요가 없기 때문에 donations 리스트에서 제거
*/
void
remove_with_lock (struct lock *lock)
{
  struct list_elem *e;
  struct thread *cur = thread_current ();

  for (e = list_begin (&cur->donations); e != list_end (&cur->donations); e = list_next (e)){
    struct thread *t = list_entry (e, struct thread, donation_elem);
    if (t->wait_on_lock == lock)
      list_remove (&t->donation_elem);
  }
}

/*
- 현재 실행중인 스레드와 그에 대한 donations 리스트에 있는 스레드들의 우선순위를 비교, 상속관계를 설정하는 함수
- 현재 실행중인 스레드의 우선순위를 init_priority에 저장
- donations 리스트가 비어있지 않을때, 일단 donations 리스트를 우선순위대로 정렬되도록 list_sort 함수 이용
- donations 리스트에서 가장 앞에있는 스레드를 가져옴(가장 앞에있는 스레드가 우선순위가 가장 높기 때문)
- donations 리스트에서 꺼낸 스레드와 현재 스레드의 우선순위를 비교하여 리스트에서 꺼낸 스레드의 우선순위가 더 높다면 cur->priority를 front->priority로 수정하여 상속 받도록 설정
*/

void
refresh_priority (void)
{
  struct thread *cur = thread_current ();

  cur->priority = cur->init_priority;
  
  if (!list_empty (&cur->donations)) {
    list_sort (&cur->donations, thread_compare_donate_priority, 0);

    struct thread *front = list_entry (list_front (&cur->donations), struct thread, donation_elem);
    if (front->priority > cur->priority)
      cur->priority = front->priority;
  }
}

/*
- **lock**을 제거하는 함수 **remove_with_lock**와 ****우선순위 상속 관계를 다시 설정하는 함수 **refresh_priority**를 이용
- **lock_release**을 통해 매개변수로 받은 lock을 지우고 지웠을 때 변경된 우선 순위대로 다시 정렬되고 상속받을수 있도록 **refresh_priority** 이용
*/
void
lock_release (struct lock *lock) {
	ASSERT (lock != NULL);
	ASSERT (lock_held_by_current_thread (lock));

	remove_with_lock (lock);
  refresh_priority ();

	lock->holder = NULL;
	sema_up (&lock->semaphore);
}
/*
- 현재 실행중인 스레드의 우선순위를 변경 하였을 때, 상속 관계가 변경될 수 있음
- 우선순위 변경시 상속 관계가 변경되는 경우
    - 예제
        - 실행되고 있는 스레드의 우선순위가 30 → 20으로 변경
        - donations에 스레드들의 우선순위가 25 - 23 - 22 일 때
        
        → 30일때는 30 > 25이기 때문에 상속받을 필요가 없었지만, 20일때는 20 < 25 이므로 상속받아 20 → 25로 우선순위 변경 필요
        
- 앞서 해당 로직을 구현한 **refresh_priority** 함수를 이용하여 다시 상속관계를 설정하여 해당 문제를 해결 가능
*/
void
thread_set_priority (int new_priority) {
	thread_current ()->init_priority = new_priority;
  
  refresh_priority ();
  thread_test_preemption ();
}

/* thread.h */
// custom
bool thread_priority_compare(const struct list_elem *a, const struct list_elem *b, void *aux);
bool thread_compare_donate_priority (const struct list_elem *l, const struct list_elem *s, void *aux UNUSED);
void donate_priority (void);
void remove_with_lock (struct lock *lock);
void refresh_priority (void);