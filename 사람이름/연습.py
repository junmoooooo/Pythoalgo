T = int(input())

def find_set(x):
    if p[x] !=x :
        p[x] = find_set[(p[x])]
    return p[x]

def union(x, y):
    if r[x] >r(y):
        p[y] = x
    else:
        p[x] = y
        if r[x] == r[y]:
            r[y] += 1

for tc in range(1, T+1):
    V,E = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(E)]
    edges.sort(key=lambda x: (x[2]))
    p = list(range(V+1))
    r = [0] *(V+1)
    ans =0
    cnt =0
    