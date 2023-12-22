matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

r = c = 1
dr = (1, -1, 0, 0)
dc = (0, 0, -1, 1)
# 하 상 좌 우
for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    print (matrix[nr][nc])


# for i in range(4):
#     nr = r + dr[i] * 2  # 2칸 가기
#     nc = c + dc[i]
#     print (matrix[nr][nc])


