T = int(input())

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x]) # path compression
    return p[x]

def union(x, y):
    if r[x] > r[y]:
        p[y] = x
    else:
        p[x] = y
        if r[x] == r[y]:
            r[y] += 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: (x[2]))
    p = list(range(V+1))
    r = [0] * (V+1)
    answer = 0
    cnt = 0

    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(find_set(s), find_set(e))
            answer += w
            cnt += 1

            if cnt == V:
                break

    print(f'#{tc} {answer}')

    #간선을 중점으로