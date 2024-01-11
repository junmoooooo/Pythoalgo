import heapq

def daextra():
    dist =[999999999] * (V+1)
    visited = set()
    heap = []
    heapq.heappush(heap, (0,0))

    while heap:
        daextra, node = heapq.heappop(heap)
        if node not in visited:
            dist[node] = daextra
            visited.add(node)

            for des in range(V+1):
                if des not in visited and dist[des] > adj[node][des] + dist[node]:
                    heapq.heappush(heap, (adj[node][des] + dist[node], des))
    return dist[V]


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    adj = [[999999999] for _ in range(V+1)]

    for i in range(E):
        st, ed, w = map(int, input().split())
    
    print(f'#{tc}',daextra())
