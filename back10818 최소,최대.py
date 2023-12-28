T = int(input())
li = list(map(int,input().split()))
max = -1000000
min = 1000001
for i in range(T):
    if li[i] > max:
        max = li[i]
    if li[i] < min:
        min = li[i]

print(f'{min} {max}')
