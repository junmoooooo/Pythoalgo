from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                initial_r, initial_c = i, j
            elif arr[i][j] == 3:
                final_r, final_c = i, j

    Q = deque([[initial_r, initial_c]])
    visited = set()
    visited.add((initial_r, initial_c))
    dist = -2
    flag = False

    while Q:
        size = len(Q)
        # 동일한 등고선에 있는 형제들을 싹다 검사하라
        for _ in range(size):
            r, c = Q.popleft()
            if r == final_r and c == final_c:
                flag = True
                Q.clear()
                break
                # clear는  for문을 break는 if문을

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and (nr, nc) not in visited:
                    Q.append([nr, nc])
                    visited.add((nr, nc))
        dist += 1
        # while문이 한번 돌때 거리가 1씩 증가한다.


    if flag:
        print(f'#{tc} {dist}')
    else:
        print(f'#{tc} {0}')


