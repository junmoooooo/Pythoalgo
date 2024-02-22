def Prim():
    dist = [9999] * (V+1)
    dist[V] = 0
    visited = [False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 99999

        for i in range(V+1):
            if not visited[i] and dist[i]< min_value:
                min_idx = i 
                min_value = dist[i]
        visited[min_idx] = True

        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]
    return sum(dist)

for tc in range(1, int(input())+1):
    V, E = map(int(input().split()))
    adj = [[9999]*(V+1) for _ in range(V+1)]

    for i in range(E):
        st, ed, w = map(int,input().split())
        adj[st][ed] = adj[ed][st] = w
