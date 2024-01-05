N = int(input())                                # NxN 배열의 N을 대입 받음

bomb = [input().rstrip() for _ in range(N)]
nobomb = [input().rstrip() for _ in range(N)]

ans = [('.'* N) for _ in range(N)]

mine = False

print(ans)
print(ans[0][1])
print(bomb)
print(bomb[0][1])
print(nobomb)

dr = [-1, 1, 0, 0, -1, -1, 1, 1]  # 8방 델타 탐색
dc = [0, 0, -1, 1, -1, 1, -1, 1]  # 상 하 좌 우 좌상 우상 좌하 우하


for r in range(N):
    for c in range(N):
        if nobomb[r][c] == 'x':
            cnt = 0
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0<= nr < N and 0 <= nc < N and bomb[nr][nc] == '*':
                    cnt += 1
                ans[r][c] = str(cnt)

                if bomb[r][c] == '*':
                    mine = True
if mine:
    for r in range(N):
        for c in range(N):
            if bomb[r][c] == '*':
                ans[r][c] = '*'


for line in ans:
    print(''.join(line))
