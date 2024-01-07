dr = (0, 1, 0 ,-1)
dc = (1, 0, -1, 0)

for tc in range(1, int(input())+1):
    N = int(input())

    snail = [[0]*N for _ in range(N)]
    r, c, d = 0, 0, 0

    for i in range(1, N**2+1):
        snail[r][c] = i
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >=N or nc < 0 or nc >=N or snail[nr][nc] != 0:
            d = (d+1)%4
            nr = r + dr[d]
            nc = c + dc[d]

        r = nr
        c = nc
    print(f'#{tc}')
    for ans in snail:

        print(*ans)




# dr = ( 0, 1, 0, -1)
# dc = ( 1, 0, -1, 0)
# # 우하좌상 ?? 여튼 내가 가고자 하는 방향을 지정
#
# for tc in range(1, int(input()) +1 ):       # tc는 테스트 케이스 몇번 문제를 풀건지
#     N = int(input()) # NxN 사이즈의 판을 깔아주기위해 N을 입력 받음
#     snail = [[0] * N for _ in range(N)]  # NxN 사이즈의 판을 깔아 달라~
#     r = 0           # r은 좌,우의 방향을 결정
#     c = 0           # c는 상,하의 방향을 결정
#     d = 0           # d는 갈 방향을 결정하기 위한 dr과 dc의 인덱스 값
#
#     for num in range(1, N**2+1):            # N*N의 판을 다 체크할 것이다.
#         snail[r][c] = num                   # 현재 달팽이의 위치를 지정
#         nr = r + dr[d]                      # 이제 정해진 방향으로 달팽이가 움직임
#         nc = c + dc[d]
#
#         if nr < 0 or nr >= N or nc <0 or nc >= N or snail[nr][nc] != 0:
#             # 달패잉가 판을 도는 조건, 판을 벗어나지 않고, 달팽이가 가는곳이 0이 아니라면?
#             d = (d + 1) % 4                 # 돌 수 있는 조건이 맞다면, 방향을 바꿀수 있게 해주자
#             nr = r + dr[d]                  # 방향을 바꾼다.
#             nc = c + dc[d]
#
#         r = nr                          # 현재 위치를 저장
#         c = nc
#
#     for ans in snail:
#         print(ans)                      # 지나온곳을 1부터해서 찍어내라