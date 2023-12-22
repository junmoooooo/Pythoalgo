# '''
# <자료구조 모양>
# 1. id값이 다 분리된 0짜리 바둑판 (2차원 리스트) 필요함
#
# 1.달팽이는 좌상단(0,0)에서 시작하여 시계방향으로 돈다
#     1-1 : 우, 하 ,좌, 상 방형으로 0, 1, 2, 3 번 방향을 잡아야함
# 2. 달팽이의 랭동
#     2-1 당팽이는 특정 칸에 도착하면 '1' 부터 숫자를 증가시키며 칸에 넣는다.
# 3. 달팽이의 방향 전환
#     3-1 : 달팽이가 뱁 밖으로 나가기전
#     3-2 : 달팽이가 갈 곳에 숫자가 이미 있을 경우
# 4. 당팽이는 방향을 아주 많이 전환 할 수 있으므로 % 연산자를 이용한다.
# '''
#
#
# # 1954_달팽이숫자
#
# dr = (0, 1, 0, -1)
# dc = (1, 0, -1, 0)
# # 시계 방향
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#
#     snail = [[0] * N for _ in range(N)]
#     r, c, d = 0, 0, 0
#     #0,0에서 0번 방향 시작
#
# 		# 1부터 N**2까지 차례로 순회하며 할당합니다.
#     for num in range(1, N ** 2 +1):
# 				# 해당 좌표에 해당 숫자를 할당합니다.
#         snail[r][c] = num
#         #현재 달팽이의 위치 에 1를 넣어 놓고 시작한다.
#
# 		# 기본적으로 기존 방향을 유지하며 다음 좌표를 설정합니다.
#         nr, nc = r + dr[d], c + dc[d]
#
# 		# 다음 좌표가 범위를 벗어나는 경우 또는 다음 좌표에 이미 숫자가 할당된 경우 방향을 전환합니다.
#         if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
#         #  snail[nr][nc] != 0 가 항상 뒤에 와야 된다.
#
# 			# 아래와 같이 방향 전환 좌표를 설정하면 3 => 0으로의 방향 전환이 가능합니다.
#             d = (d + 1) % 4
#             nr, nc = r + dr[d], c + dc[d]
#
# 				# 위에서 계산한 다음 좌표를 현재 좌표로 최신화한 후 다음 반복으로 넘어갑니다.
#         r, c = nr, nc
#
#     print(f'#{tc}')
#     for ans in snail:
#         print(*ans)



#단축평가
# 1 and 5
# 5
# 0 and 7
# 0
# 3 or 4
# 3
# 0 or 9
# 0

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input())+1):
    N= int(input())

    filed = [[0]* N for _ in range(N)]   # 판깔아줘
    r= 0
    c= 0
    d= 0

    for num in range(1, N**2+1):
        filed[r][c] = num

        nr = r + dr[d]
        nc = c + dc[d]

        if (nr < 0 or nr >= N) or (nc <0 or nc >= N) or filed[nr][nc] != 0:
            d = (d + 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]

        r= nr
        c= nc

    print(f'#{tc}')
    for ans in filed:
        print(*ans)