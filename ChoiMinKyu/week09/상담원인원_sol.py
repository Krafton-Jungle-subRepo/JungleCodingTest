from collections import defaultdict
from collections import Counter
from itertools import combinations_with_replacement
import heapq
def solution(k, n, reqs):
    reqs.sort(key=lambda x : x[0])
    
    dic = defaultdict(list)
    for a,b,c in reqs:
        dic[c].append([a,b])
    #print(dic)
    
    arr = [i for i in range(1,k+1)]
    combi = list(combinations_with_replacement(arr, n))
    
    answer = 987654321
    for c in combi:
        counter = Counter(c)
        if len(counter) == k: # 무조건 유형개수 만큼은 멘토를 배정해야함.
            #print(counter)
            wait = 0
            for key,vs in dic.items():
                #print(key, vs)
                heap = []
                for i in range(len(vs)):
                    start = vs[i][0]
                    time = vs[i][1]
                    if i < counter[key]: # 유형 개수만큼 큐생성
                        heapq.heappush(heap, start+time)                        
                    elif i >= counter[key] and len(heap)>0:
                        end = heapq.heappop(heap)  
                        if end <= start: # 끝나는 시간이 50이고 내가 들어가는 시간이 50면 대기시간없음
                            heapq.heappush(heap, start+time)
                        else: # 끝나는 시간이 70이고 내가 들어가는 시간이 65면 대기시간 구함
                            wait += end - start
                            heapq.heappush(heap, end+time)
                    #print(i, heap, wait)
            if wait < answer:
                answer = wait
    return answer

k = 3
n = 5
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]

print(solution(k,n,reqs))