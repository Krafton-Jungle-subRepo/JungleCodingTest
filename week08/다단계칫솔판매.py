import sys
input = sys.stdin.readline

def solution(enroll, referral, seller, amount):
    graph = []
    selling_list = {}

    # 딕셔너리로 selling_list 구현 {셀러:수익}
    for i in range(len(seller)):
        selling_list[seller[i]] = amount[i]*100

    for i in range(len(enroll)):
        cost = selling_list.get(enroll[i])
        if cost==None:
            cost = 0
        graph.append((enroll[i],referral[i],cost))

    answer = [0]*((len(enroll))+1)

    for i in range(len(graph)):
        e,r,cost = graph[i]
        
        rest = cost*0.1
        graph[i][2] += int(cost - rest)



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