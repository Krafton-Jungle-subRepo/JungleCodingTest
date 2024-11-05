def solution(enroll, referral, seller, amount):
    
    parent = {}
    res = {}
    for i in range(len(referral)):
        parent[enroll[i]] = referral[i]
        res[enroll[i]] = 0

    def findRoot(child, cost):
        while (cost >= 1): 
            give_to_parent = cost // 10
            res[child] += cost - give_to_parent
            child = parent[child]
            cost = give_to_parent
            if child == '-':
                break

    for i in range(len(seller)):
        findRoot(seller[i], amount[i]*100)

    answer = list(res.values())
    return answer