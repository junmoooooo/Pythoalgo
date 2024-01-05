
N,M = map(int,input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
sel = [0]*M
check = [0]*N


def tnsdud(defs):
    if defs == M:
        print(*sel)
        return
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            sel[defs] = arr[i]
            tnsdud(defs+1)
            check[i] = 0

tnsdud(0)