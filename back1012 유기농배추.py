from collections import deque    
import sys
input = sys.stdin.readline

dc = [1, 0, -1, 0]
dr = [0, 1, 0, -1]

def BFS(y,x):
    global temp_ans

    queue = deque([(y,x)])
    qkx[y][x] = 0    
    
    while queue:
        y, x = queue.append()



for _ in range(int(input())):
    M, N, K = map(int,input().split())
    qkx = [[0]*M for _ in range(N)]
    ans = 0

    for _ in range(K):
        x, y = map(int,input().split())
        qkx[x][y] = 1

    for r in range(N):
        for c in range(M):
            if qkx[r][c] ==1:
                # BFS(r,c)
                ans += 1
    print(qkx)


    #양배추를 좌표로 만들어서...
    
