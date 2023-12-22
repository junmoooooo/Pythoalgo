def dfs(n):
    if n not in visited:  # 우선 visited 없으면 넣어줌
        visited.append(n)

    for destination in range(V+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)  # 다음 재귀 깊이로 이동

V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

visited = []  # 궤적 기록용

dfs(1)  # 1번 포도알부터 시작!

print('이동경로:', *visited)

# 이동경로: 1 2 4 6 5 7 3 => 이거 다른거 주의!!
# main이 종료되어야 sub가 실행된다는 것을 생각
# 다음 main은 이전 main의 sub임
# (main) (sub1) (sub2) ...
# 1
# 1-2 / 1-3
# 1-2-4 / 1-2-5 / 1-3
# 1-2-4-6 / 1-2-4-5 / 1-2-5 / 1-3
# 1-2-4-6-5 / 1-2-4-6-7 / 1-3 # main이 5를 갔으니 sub 1-2-5, sub 1-2-4-5는 시작도 못함
# (1-2-4-6-5) / 1-2-4-6-7 / 1-3 # main 종료 및 기록됨, 이전 main 1-2-4-6이 main이 됨
# (1-2-4-6-5)-7 / 1-3 # main이 7을 갔으니 sub 1-2-4-6-7은 시작도 못함
# (1-2-4-6-5)-7-3 # main이 3을 갔으니 sub 1-3은 시작도 못함
# main 종료, sub는 없음