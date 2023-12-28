tree = list(map(int,input().split()))

while tree != [1, 2, 3, 4, 5 ] :
    for i in range(1,len(tree)):
        # 0부터 찾으면 i-1이 -1이 되면서 배열의 마지막 걸 가져오자나@!!
        if tree[i-1] > tree[i]:
            tree[i],tree[i-1] = tree[i-1],tree[i]
            print(*tree)



