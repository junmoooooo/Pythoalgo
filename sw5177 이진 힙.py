import heapq
from builtins import range

for tc in range(int(input())):
    N = int(input())
    arry = list(map(int,input().split()))

    heapq.heapify(arry)
    print(arry)

    asum = 0

    for i in range(1, len(arry)+1, len(arry)//2):
        asum += arry[i]
        print(asum)