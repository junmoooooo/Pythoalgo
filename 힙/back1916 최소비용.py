import sys
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra(start):                    # 힙큐를 활용한 다익스트라
    visited = set()
    heap = []
    heappush(heap, (0, start))

    while heap:                         # 힙이 다 돌 때까지
        d, now = heappop(heap)          # 현재 가장 짧은 거리와 위치를 꺼내서

        if now not in visited:          # 방문한 적이 없다면
            dist[now] = d               # 거리를 갱신하고
            visited.add(now)            # 방문지 표시

            for after, tmp_d in dist_info[now]:     # 다음 방문 후보지 탐색
                if after in visited:                # 이미 방문한 곳은 빼고
                    continue

                if dist[after] > d + tmp_d:   # 이번에 갱신을 통해 더 짧은 거리가 탐색되었다면
                    heappush(heap, (d + tmp_d, after))    # 힙에 넣기
    return dist[E]

N = int(input())
M = int(input())

dist_info = [[] for _ in range(N+1)]        # 인접 리스트로 구조화

for _ in range(M):
    s, e, c = map(int, input().split())
    dist_info[s].append((e, c))

S, E = map(int, input().split())
dist = [987654321] * (N+1)

print(dijkstra(S))                            # 출발지 기준 다익스트라
# print(dist[E])                              # 목적지까지 최소거리 출력

#다익스트라를 이용한 최소비용