dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input()) + 1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]
    r, c, d = 0, 0, 0
		# 1부터 N**2까지 차례로 순회하며 할당합니다.
    for num in range(1, N ** 2 + 1):
				# 해당 좌표에 해당 숫자를 할당합니다.
        snail[r][c] = num

				# 기본적으로 기존 방향을 유지하며 다음 좌표를 설정합니다.
        nr, nc = r + dr[d], c + dc[d]

				# 다음 좌표가 범위를 벗어나는 경우 또는 다음 좌표에 이미 숫자가 할당된 경우 방향을 전환합니다.
        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
						# 아래와 같이 방향 전환 좌표를 설정하면 3 => 0으로의 방향 전환이 가능합니다.
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]

				# 위에서 계산한 다음 좌표를 현재 좌표로 최신화한 후 다음 반복으로 넘어갑니다.
        r, c = nr, nc

    print(f'#{tc}')

    for ans in snail:
        print(*ans)