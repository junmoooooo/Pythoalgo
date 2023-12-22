#버블 정렬    N-1회

# arr = [2, 4, 1, 3]
#
# for i in range(len(arr)-1,0,-1):
#     for j in range(i):
#         if arr[j] > arr [j+1]:
#             arr[j], arr[j+1]  = arr[j+1], arr[j]
#
# 이중배열 버블
# a= [[4,4,16], [6,1,6], [4,3,12], [1,12,12], [5,4,20], [2,3,6], [3,4,12]]
#
# def bubble_sort(idx):
#
#     for i in range(len(a)-1,0,-1):
#         for j in range(i):
#             if a[j][idx] > a[j+1][idx]:
#                 a[j], a[j+1] = a[j+1], a[j]
#
#
# bubble_sort(1)
#
# sorted_a = sorted(a, key=lambda x:x[1])
# print(sorted_a)

#카운팅 정렬 코드
nums =[4,4,2,3,5,5,1,1,5]

count = [0]* (max(nums)+1)
sorted_nums = [0] * len(nums)

for num in nums:
    count[num] += 1

for i in range(1, len(count)):
    count[i] = count[i] + count[i-1]

for j in range(len(nums)-1,-1,-1):
    sorted_nums[count[nums[j]]-1] = nums[j]
    count[nums[j]] -= 1

print(sorted_nums)