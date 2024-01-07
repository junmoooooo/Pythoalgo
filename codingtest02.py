V = int(input()) # 노드 갯수

network = [[] for _ in range(V + 1)]  # 인접리스트 기본틀

for _ in range(V-1):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    network[start].append(end)
    network[end].append(start)  # 양방향 그래프니까!!

stack = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용



while stack:  # 스택이 빌때까지 돌아라!
    cnt= 0
    qlryrns = 0
    current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌

    for destination in network[current]:
        if destination not in visited:  # 갈 수 있고 + 방문 안했으면!
            stack.append(destination)  # 다음 갈 곳으로 Stack에 저장
            cnt += 1
        print(cnt)


# 노드 갯수 받고
# 전선의 수는 노드 -1
# dfs로 비지티드 갯수를 구하는데
# 전선을 자르는걸 구현을 어떻게하지?
# 전선을 임의로 하나 잘라보고 각 위치에서 제일 큰 비지티드랑 
# 제일 작은 비지티드의 차이가 제일 작은 값을 출력
