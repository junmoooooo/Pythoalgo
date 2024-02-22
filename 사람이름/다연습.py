import heapq

def ekdlrtm():
    dist = [9999] * (V+1)
    visited = set()
    chlth= []
    heapq.heappush(chlth,(0,0))

    while chlth:
        distance, node = heapq.heappop(chlth)
        if node not in visited:
            dist[node] = distance
            visited.add(node)

            for destination in range(V+1):
                if destination not in visited and dist[destination] > adj[node][destination] + dist[node]:
                    heapq.heappush(chlth, (adj[node][destination] + dist[node] + destination))


    return dist[V]

for tc in range (1, int(input())+1):
    V, E = map(int,input().split())
    adj =[[9999]*(V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed, w = map(int,input().split())
        adj[st][ed] = w

    print()