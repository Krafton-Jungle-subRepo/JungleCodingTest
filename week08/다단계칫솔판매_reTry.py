import sys
input = sys.stdin.readline

def calculate(parent, child,cost,res):
    while (cost >= 1):
        res[child] += cost - cost//10
        child = parent[child]
        if (child == '-'):
            break
        cost = cost//10

def solution(enroll, referral, seller, amount):
    answer = []

    res = {}
    parent = {}

    # 딕셔너리로 parent {자식:부모}, res 구현 {셀러:수익}
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        res[enroll[i]] = 0

    for i in range(len(seller)):
        calculate(parent,seller[i],amount[i]*100,res)

    answer = [res[name] for name in enroll]

    return answer

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