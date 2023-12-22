dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
#델타 탐색은 미리 적어 놓자
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for r in range(N):
        for c in range(M):
            tmp = board[r][c]                       # 일단 해당 위치 더하고

            for d in range(4):                      # 사방을 탐색하며
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:     # 범위 내에 있다면
                    tmp += board[nr][nc]            # 더해주고

            ans = max(ans, tmp)                     # 갱신

    print(f'#{tc} {ans}')





# board = [[0 for _ in range(M+2)]for _ in range(N+2)]
#     for i in range(1, N+1):
#         board[i][1:M+1] = map(int,input().split())

