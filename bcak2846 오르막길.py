N =int(input())
load = list(map(int,input().split()))

now=0
up=0

for i in range(1, N):
    if load[i-1] < load[i]:
        now += load[i] - load[i-1]
        up = max(now, up)
    else:
        now = 0

print(up)