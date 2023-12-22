# matrix = [[3, 7, 9],[4, 2, 6],[8, 1, 5]]
#
# print(matrix)
#
# N= 3
#
# for i in range(N**2):
# 	print(matrix[i//N][i%N], end=' ')
#
# matrix = [[3, 7, 9],
# 		[4, 2, 6],
# 	    [8, 1, 5]]
#
# for r in range(3):
#     for c in range(3):
#         if r > c: # r < c로 해도 됩니다.
#             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
#
# for i in range(3):
#     print(matrix[i])
#


#ZIP
matrix = [[3, 7, 9],[4, 2, 6],[8, 1, 5],[10,11,12]]
print(list(zip(matrix[0],matrix[1],matrix[2],matrix[3])))

c = [[1,2], [3,4]]
print(list(zip(*c)))

print(dict(zip(range(3), [0]*3))) # {0: 0, 1: 0, 2: 0}