# def fibo(n):
#     if n<2:     # 1은 더 쪼개지지 않음
#         return n
#     else:
#         print(n)
#         return  fibo(n-1) + fibo(n-2)  #재귀호출
#
#
# print(fibo(10))
#
#
# #메모이제이션
# memo = [0, 1]
#
# def fibo(n):
#     if n >= 2 and n >= len(memo):
#         memo.append(fibo(n-1) + fibo(n-2))
#     return memo[n]
#
# print(fibo(10))


#이진검색
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def binary_search(low, high, target):
#     if low > high:
#         return '찾지 못함'
#
#     mid = (low + high) // 2
#     if target == nums[mid]:
#         return mid+1
#     elif target < nums[mid]:
#         return binary_search(low, mid-1, target)
#     elif target > nums[mid]:
#         return binary_search(mid+1, high, target)
#
# print(binary_search(0, len(nums)-1, 8))




#분할 정복
def power(base, exponent):
    if exponent == 1:
        return base

    x = power(base, exponent// 2)
    if exponent % 2:
        return  x * x * base
    else :
        return x * x

print(power(2, 5))
