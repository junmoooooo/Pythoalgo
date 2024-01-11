T = int(input())

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])

def union(x,y):
    if r[x] > r[y]:
        p[y] += 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    