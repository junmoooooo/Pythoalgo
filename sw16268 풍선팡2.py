dr = (0, 1, 0, -1)
dc = (1, 0 ,-1, 0)

for tc in range(int(input())):
    N, M = map(int,input().split())
    pang = [list(map(int,input().split()))for _ in range(N)]

    print(pang)
    ans = 0

    for r in range(N):
        for c in range(M):                         # N*M 만큼 돌거야
            tmp = pang[r][c]                       # 일단 해당 위치를 저장하고

            for d in range(4):                     # 사방을 탐색하며
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:    # 범위 내에 있다면
                    tmp += pang[nr][nc]            # 현재 위치에 사방탐색을 한 숫자를 더해주고

            ans = max(ans, tmp)                     # 갱신

    print(f'#{ans}')

#정답