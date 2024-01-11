# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#
#     for x in range(N - M + 1):          # (0, 0) ~ ((N-M), (N-M)) 까지 완전 탐색
#         for y in range(N - M + 1):
#             tmp = sum(board[i][j] for i in range(x, x + M) for j in range(y, y + M))    # 해당 위치에서 +M씩 더하기
#             ans = max(tmp, ans)         # 최대값 갱신
#
#     print(f"#{tc} {ans}")



T = int(input())

for a in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    kills = []
    # 파리채를 내려칠 곳 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 근데 인간적으로 이걸 어떻게 머리로 생각해 낼수 가 있는거지?
            # 그냥 N으로 돌리면 파리채가 범위를 벗어나게 떄려버리는 구나...
            fly = 0
            # 해당 위치를 타격했을 때 잡을 수 있는 파리의 수 탐색
            for k in range(M):
                for l in range(M):
                    fly += arr[i+k][j+l]
            kills.append(fly)
	# 배열 범위 안에서 가능한 경우의 수 중에서 가장 많은 파리를 잡을 때의 수 출력
    print("#"+str(a+1), max(kills))