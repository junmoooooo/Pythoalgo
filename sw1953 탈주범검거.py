# from collections import deque

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# # 각 파이프가 갈 수 있는 방향 및 해당 방향으로 연결될 수 있는 파이프 구조화
# pipe_info = {
#     1: [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]],
#     2: [[1, 2, 5, 6], [1, 2, 4, 7], [], []],
#     3: [[], [], [1, 3, 4, 5], [1, 3, 6, 7]],
#     4: [[1, 2, 5, 6], [], [], [1, 3, 6, 7]],
#     5: [[], [1, 2, 4, 7], [], [1, 3, 6, 7]],
#     6: [[], [1, 2, 4, 7], [1, 3, 4, 5], []],
#     7: [[1, 2, 5, 6], [], [1, 3, 4, 5], []]
#     }

# for tc in range(1, int(input()) + 1):
#     N, M, R, C, L = map(int, input().split())
#     underground = [list(map(int, input().split())) for _ in range(N)]

#     # 출발지 큐에 집어넣기
#     queue = deque([(R, C, 0)])
#     visited = set()

#     while queue:

#         r, c, cnt = queue.popleft()

#         if cnt == L:                    # L시간이 나왔음은 L-1시간까지 탐색 가능한 모든 파이프가 방문지에 담겼음을 의미
#             break                       # 탐색 중단

#         visited.add((r, c))             # 아니라면 방문지에 담고

#         for d in range(4):
#             nr, nc = r + dr[d], c + dc[d]

#             # 범위를 벗어났거나, 방문한 곳이거나, 파이프가 없다면 통과
#             if nr < 0 or nr >= N or nc < 0 or nc >= M or (nr, nc) in visited or underground[nr][nc] == 0:
#                 continue

#             # 다음 갈 곳의 파이프 종류가 현재 파이프에서 갈 수 있는 곳이고, 연결 가능한 곳이라면
#             if underground[nr][nc] in pipe_info[underground[r][c]][d]:
#                 # 큐에 담기
#                 queue.append((nr, nc, cnt+1))

#     print(f'#{tc} {len(visited)}')  # 정답은 방문지의 길이



from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]

    # 출발지 큐에 집어넣기
    queue = deque([(R, C, 0)])
    visited = set()

    while queue:

        r, c, cnt = queue.popleft()

        if cnt == L:                    # L시간이 나왔음은 L-1시간까지 탐색 가능한 모든 파이프가 방문지에 담겼음을 의미
            break                       # 탐색 중단

        visited.add((r, c))             # 아니라면 방문지에 담고

        if underground[r][c] == 1:      # 1번 파이프
            direction = [0, 1, 2, 3]    # 상하좌우 이동 가능

        elif underground[r][c] == 2:    # 2번 파이프
            direction = [0, 1]          # 상하 이동 가능
            
        elif underground[r][c] == 3:    # 3번 파이프
            direction = [2, 3]          # 좌우 이동 가능

        elif underground[r][c] == 4:    # 4번 파이프
            direction = [0, 3]          # 상우 이동 가능

        elif underground[r][c] == 5:    # 5번 파이프
            direction = [1, 3]          # 하우 이동 가능

        elif underground[r][c] == 6:    # 6번 파이프
            direction = [1, 2]          # 하좌 이동 가능

        elif underground[r][c] == 7:    # 7번 파이프
            direction = [0, 2]          # 상좌 이동 가능

        for i in direction:             # 이동이 가능한 방향만 고려
            nr, nc = r + dr[i], c + dc[i]

            # 범위를 벗어나거나, 방문한 곳이거나, 파이프가 없는 곳이라면 이동 중지
            if nr < 0 or nr >= N or nc < 0 or nc >= M or (nr, nc) in visited or underground[nr][nc] == 0:
                continue

            # 현재 방향이 '상'이라면 1, 2, 5, 6 파이프로 이동 가능
            elif i == 0 and underground[nr][nc] in [1, 2, 5, 6]:
                queue.append((nr, nc, cnt+1))

            # 현재 방향이 '하'라면 1, 2, 4, 7 파이프로 이동 가능
            elif i == 1 and underground[nr][nc] in [1, 2, 4, 7]:
                queue.append((nr, nc, cnt+1))

            # 현재 방향이 '좌'라면 1, 3, 4, 5 파이프로 이동 가능
            elif i == 2 and underground[nr][nc] in [1, 3, 4, 5]:
                queue.append((nr, nc, cnt+1))

            # 현재 방향이 '우'라면 1, 3, 6, 7 파이프로 이동 가능
            elif i == 3 and underground[nr][nc] in [1, 3, 6, 7]:
                queue.append((nr, nc, cnt+1))

    print(f'#{tc} {len(visited)}')  # 정답은 방문지의 길이