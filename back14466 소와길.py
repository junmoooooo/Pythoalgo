N, K, R = map(int,input().split())

road =[[] for _ in range(N+1)]
cox =[]

for _ in range(R):
    xs, ys, dx, dy = map(int,input().split())
    road[(xs,ys)].append((dx,dy))
    

for _ in range(K):
    c = list(map(int,input().split()))
    cox.append(c)

print(cox)
print(road)