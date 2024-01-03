arry=[]
sell=[]
N,M = map(int,input().split())

for i in range(1, N+1):
    arry.append(i)
for j in range(M):
    sell.append(0)

def combination(idx, sidx):
    if sidx == M:
        print(*sell)
        return
    if idx == N:
        return
    
    sell[sidx] = arry[idx]
    combination(idx+1,sidx+1)
    combination(idx+1,sidx)


combination(0,0)