matrix = [ [1, 2, 3],[4, 5, 6],[7, 8, 9] ]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]  #초기화

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]
# rotated_matrix 결과

print(rotated_matrix)