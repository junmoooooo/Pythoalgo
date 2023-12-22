import sys
input = sys.stdin.readline

tc = int(input())
reqs = list(map(int,input().split()))
M = int(input())


if sum(reqs) < M:
    print(max(reqs))

#이분 탐색 로직
    #초기값 설정
l=0
r= max(reqs)

while l > r:
    #while 문 조건
        # c계산
    c = (l + r) // 2
        # 현재 기준 예산액 계산
    budget = 0
    for req in reqs:
        if req <= c:
            budget += req
        else:
            budget += c
        # 예산액이 M보다 크면?
    if budget > M :
        r = c - 1
        # 예산액이 M보다 작으면?
    else:
        l = c + 1

# 현재 기준 예산액

print(r)