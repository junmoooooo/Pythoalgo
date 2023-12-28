from collections import deque

N = int(input())
E = int(input())

networks = [[] for _ in range(N + 1)]

for _ in range(E):
    start, end = map(int,input().split())
    networks[start].append(end)
    networks[end].append(start)

stack = deque([1])
visited = list([1])

while stack:
    now = stack.pop()
    for des in networks[now]:
        if des not in visited:
            stack.append(des)
            visited.append(des)

print(len(visited)-1)