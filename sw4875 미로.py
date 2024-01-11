from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]                  # 우 하 좌 상

for tc in range(int(input())):
    N = int(input())
    pan = [list(map(int,input().rstrip())) for _ in range(N)]

    stack = deque()
    r, c, d = 0, 0, 0
    miro = False

    # 여기 까지가 내가 필요한 것들 만들어 놓은 거고
    for r in range(N):
        for c in range(N):
            if pan[r][c] == 2:              # 출발지를 탐색하여
                stack.append((r, c))        # stack에 넣어주고
                break
        if stack:
            break
    # 출발지를 따로뽑아 쓰기 위해 스택에 넣어주는걸 따로 쓰는거 같음
    # 그리고 스택을 이용하여 출발지 부터 탐색해서 탐색이 끝난 곳은 다시 방문 못하도록 만들어야지
    # visited를 사용하지 않음

    while stack:
        r, c = stack.pop()                  # 갈곳을 스택에서 뽑아서

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 방향 설정해주고
            if 0<= nr < N and 0<= nc < N and pan[nr][nc] != 1:
                stack.append((nr,nc))           # 다음 갈 곳을 stack에 넣어주고
            #사방 탐색
        if pan[r][c] == 3:                  # 도착한곳이 3이면 미로가 True
            miro = True
            break
        pan[r][c] = 1               # 내가 지나온곳을 1로 만들어 재방문 방지

    if miro:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')

