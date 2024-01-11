N = int(input())

def vorxhfldjf(num):
    i = 0
    if num != 0:

        i = num*vorxhfldjf(num-1)
        return i

    if num == 0:
        return 1

print(vorxhfldjf(N))


#
# N = int(input())
#
#
# def my_factorial(n):
#
#     i =0
#     if n <= 1:  # 1보다 작거나 같은 경우 1을 return
#         return 1
#
#     else:  # 1보다 큰 경우 n-1로 재귀
#         i = n * my_factorial(n - 1)
#         return (i)
#
# print(my_factorial(N))