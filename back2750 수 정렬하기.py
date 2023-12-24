TC = int(input())
nums =[]

for i in range(TC):
    num = int(input())
    nums.append(num)

nums.sort()

for i in range(len(nums)):
    print(nums[i])