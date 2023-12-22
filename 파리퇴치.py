for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for x in range(N - M + 1):          # (0, 0) ~ ((N-M), (N-M)) 까지 완전 탐색
        for y in range(N - M + 1):
            tmp = sum(board[i][j] for i in range(x, x + M) for j in range(y, y + M))    # 해당 위치에서 +M씩 더하기
            ans = max(tmp, ans)         # 최대값 갱신

    print(f"#{tc} {ans}")



