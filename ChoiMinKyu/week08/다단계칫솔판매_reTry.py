# 빠른 입력을 위해 sys.stdin 사용
import sys
input = sys.stdin.readline
# 부모를 타고 올라가며 금액 계산
def calculate(parent, child,cost,res):
    while (cost >= 1):
        res[child] += cost - cost//10
        child = parent[child]
        if (child == '-'):
            break
        cost = cost//10

def solution(enroll, referral, seller, amount):
    # 결과 할당 할 배열
    answer = []

    # 결과 할당 할 딕셔너리, 자식에 대해 부모들을 나타낼 딕셔너리
    res = {}
    parent = {}

    # 딕셔너리로 parent {자식:부모}, res 구현 {셀러:수익}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        res[enroll[i]] = 0
    # seller 배열에서 값 하나씩 꺼내 calculate() 함수로 전달
    for i in range(len(seller)):
        calculate(parent,seller[i],amount[i]*100,res)
    # enroll의 순서에 맞게 answer에 값 할당
    answer = [res[name] for name in enroll]
    # 결과 리턴
    return answer

### 출력 테스트
# 각 판매원의 이름
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# 각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# 판매량 집계 데이터의 판매원의 이름
seller = ["young", "john", "tod", "emily", "mary"]
# 판매량 집계 데이터의 판매 수량
amount = [12, 4, 2, 5, 10]

result = solution(enroll, referral, seller, amount)
print(result)