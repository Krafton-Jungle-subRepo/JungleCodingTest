def solution(k, n, reqs):
    answer = 0

    from itertools import product
    import heapq
    import sys

    m = len(reqs)

    def find_partitions(n, k):
        res = []
        for nums in product(range(1, n-k+2), repeat=k):
            if sum(nums) == n:
                res.append(nums)
        return res

    partitions = find_partitions(n, k)

    def findReqs():
        global ansewer
        minTime = sys.maxsize
        
        for partition in partitions:
            queues = [[0] * num for num in partition]
            total_wait = 0
            for req in reqs: 
                wait_time, duration, typenum = req
                popped = heapq.heappop(queues[typenum-1])
                if(popped > wait_time):
                    total_wait += popped - wait_time
                    heapq.heappush(queues[typenum-1], duration + popped)
                else:
                    heapq.heappush(queues[typenum-1], duration + wait_time)

            minTime = min(minTime, total_wait)
            
        return minTime


    answer = findReqs()
    return answer


k = 3
n = 5
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
print(solution(k, n, reqs))