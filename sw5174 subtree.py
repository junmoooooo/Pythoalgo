for tc in range(int(input())):
    E, N = map(int,input().split())
    edges = list(map(int,input().split()))

    left = [0] * (E+2)          # 자식을 이용해서
    right = [0] * (E+2)         # 부모를??
    ancestors = [0] * (E+2)     # 조상 

    sfs =[]

    for i in range(E):
        parent, child = edges[i*2], edges[i*2+1]
        if not left[parent]:      
            left[parent] = child
            # 부모를 기준으로 자식을 정하기
        else:
            right[parent] = child
            # 자식을 기준으로 부모를 정하기?
            
        ancestors[child] = parent

    root = None
    for j in range(1, E+2):
        if ancestors[j] == 0:
            root = j
            break

    def preorder(root):
        if root > 0:
            sfs.append(root)
            # print(root, end=' ')
            preorder(left[root])
            preorder(right[root])

    preorder(N)
    print(f'#{tc+1}', len(sfs))
    