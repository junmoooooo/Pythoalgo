import sys
input = sys.stdin.readline

from heapq import heappush, heappop

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra(r, c):                             # 델타탐색 + 다익스트라
    heap = []
    check[r][c] = 0
    heappush(heap, (arr[r][c], 0, 0))
    
    while heap:
        BR, r, c = heappop(heap)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                NBR = BR + arr[nr][nc]              #델타 탐색을 하면서
                if check[nr][nc] > NBR:
                    check[nr][nc] = NBR             #조건이 맞으면 최소를 갱신
                    heappush(heap, (NBR, nr, nc))   #다음에 넣을 것도 갱신

tc = 0
while True:
    N = int(input())
    if N == 0:
        break

    tc += 1

    arr = [list(map(int, input().split())) for _ in range(N)]
    check = list([987654321] * N for _ in range(N))

    dijkstra(0, 0)

    print(f'{"Problem"} {tc}{":"} {check[N-1][N-1]}')