def Prim():
    dist = [999999999] * (V+1)
    dist[N] = 0
    visited =[False] * (V+1)

    for _ in range(V+1):
        min_idx = -1
        min_value = 999999999

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx =i
                min_value = dist[i]

        visited[min_idx] = True
        print(visited, dist)

        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]

    return sum(dist)



for tc in range(1, int(input())+1):
    N, V, E = map(int,input().split())

    adj = [[999999999] * ( V+1) for _ in range(V + 1)]

    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = adj[ed][st] = w

    print("#{} {}".format(tc, Prim()))    