import math
n = list(str(input()))
nums = [0 for _ in range(10)]

for i in range(len(n)):
    num = int(n[i])
    nums[num] += 1
sixnine = math.ceil((nums[6] + nums[9]) / 2)

nums.pop(9)
nums.pop(6)
print(max(max(nums), sixnine))