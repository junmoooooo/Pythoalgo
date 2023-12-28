import sys
input = sys.stdin.readline

from collections import deque

N = int(input())                            # 노드 숫자
E = int(input())                            # 간선 숫자

adj = [[] for _ in range(N + 1)]            # 인접 리스트 빈 판
# 0번 컴퓨터가 없으므로 N+1
for _ in range(E):                          # 간선 숫자만큼 돌면서
    start, end = map(int, input().split())  # 간선 정보 입력받아
    adj[start].append(end)                  # 인접 리스트에 입력
    adj[end].append(start)                  # (양방향 그래프이므로)

stack = deque([1])                          # 1에서 시작하므로 스택에 넣고 시작
visited = set([1])                          # 방문지 담아줄 set

while stack:                                # 스택이 빌 때까지
    now = stack.pop()                       # 오른쪽에서 뽑아서

    for destination in adj[now]:            # 해당 컴퓨터에서 이동할 수 있는 컴퓨터들 가운데
        if destination not in visited:      # 아직 방문하지 않은 곳이 있다면
            stack.append(destination)       # 스택에 넣고
            visited.add(destination)        # 방문지에 넣기

print(len(visited) - 1)                     # 정답은 방문지 - 1(1번 컴퓨터 제외)


# 부분 집합 문제? 그래프의 특정 어쩌구? 




#DFS(인접 리스트 + 재귀)로 풀기

# import sys
# input = sys.stdin.readline

# def dfs(now):                               # 재귀 함수
#     if now not in visited:                  # 현재 위치가 방문지에 없다면,
#         visited.add(now)                    # 방문지에 추가하고

#     for after in adj[now]:                  # 갈 수 있는 모든 곳들에 대해
#         if after not in visited:            # 가본적이 없다면
#             dfs(after)                      # 재귀

# N = int(input())
# E = int(input())

# adj = [[] for _ in range(N + 1)]            # 인접 리스트 빈 판
# for _ in range(E):                          # 간선 숫자만큼 돌면서
#     start, end = map(int, input().split())  # 간선 정보 입력받아
#     adj[start].append(end)                  # 인접 리스트에 입력
#     adj[end].append(start)                  # (양방향 그래프이므로)

# visited = set()

# dfs(1)                                      # 1번 노드에서 시작

# print(len(visited) - 1)                     # 정답은 방문지 - 1(1번 컴퓨터 제외)