# SWEA 5251 최소 이동 거리 풀이
import heapq

def dijkstra():
    dist = [987654321] * (V+1)
    visited = set()  # 효율화를 위한 셋
    heap = []  # 빈 리스트 하나 생성해서 최소힙 자료구조로 활용
    heapq.heappush(heap, (0, 0))  # (거리, 노드번호)

    while heap:  # 힙이 빌때까지 돌아라
        distance, node = heapq.heappop(heap)  # 거리와 노드번호를 뽑고 (뽑힌 순간 최소 거리로 뽑혔을 것)
        if node not in visited:  # visited 없는 경우에 한해서 + visited 되지 않은 경우는 바로 다음 힙팝이 실행될 것!
            dist[node] = distance  # 최소힙에서 뽑았으니까 바로 그녀석의 distance가 최소 이동 거리일것
            visited.add(node)  # visited 도장을 찍어준다
	
            for destination in range(V+1):  # 현재의 node에서 갈 수 있는 destination을 모두 체크할건데,
                # 아직 방문하지 않았어야 함과 동시에
                # 목적지까지의 기존 이동거리라고 생각했던 것 > 내 위치까지의 이동거리 + 내 위치로부터 목적지까지의 이동거리를 만족하면
                if destination not in visited and dist[destination] > adj[node][destination] + dist[node]:
                    heapq.heappush(heap, (adj[node][destination] + dist[node], destination))  # 최소힙에 넣어라!

    return dist[V]


for tc in range(1, int(input())+1):
    V, E = map(int,input().split())

    adj = [[987654321] * (V+1) for _ in range(V+1)]  # inf 개념으로 큰 수 넣어줌

    for i in range(E):  # 인접행렬 만들기
        st, ed, w = map(int, input().split())
        adj[st][ed] = w  # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print("#{} {}".format(tc, dijkstra()))