TC = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

n=0
nums=[]


for i in range(TC):
    n = max(B)*min(A)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
    nums.append(n)

print(sum(nums))