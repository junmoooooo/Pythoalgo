
N = int(input())
contry = [list(map(int, input().split())) for _ in range(N)]
ans = 987654321
check = [0] * N



print(contry)

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dfs(now, distance, depth):
    global ans

    if depth == N:
        distance += dist(contry[now], contry[0])
        ams =min(distance, ans)
        return
    if distance >ans:
        return
    
    for after in range(N):
        if not check[after] :
            check[after] = 1
            dfs(after, distance+dist(contry[now], contry[after]), depth +1)
            check[after] = 0

    for i in range(N):
        dfs(i, dist(contry[0], contry[i]), 0) 

    print(ans)

    
dfs(0,0,1)