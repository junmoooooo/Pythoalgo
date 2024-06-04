for tc in range(int(input())):
    E, R = map(int,input().split())
    rkstjs = list(map(int,input().split()))             # 입력받을 거 입력받고

    left = [0] * (E+2)                                  # 노드의 갯수+1 만크 left와
    right = [0] * (E+2)                                 # right
    whtkd = [0] * (E + 2)                               # whtkd을 리스토 만들어 놓고

    for i in range(E):                                  # 간선의 수만큼 반복해서
        p, c = rkstjs[i*2], rkstjs[i*2+1]               # 부모와 자식을 구별
        if not left[p]:                                 # p의 left가 비어있다면,
            left[p] = c                                 # p의 left가 c
        else:                                           # p의 left가 비어있지 않다면,
            right[p] = c                                # p의 right가 c

        whtkd[c] = p                                    # c의 부모는 p
    # 여기까지가 이진 트리를 만들었다고 보면되고,

    root = None                                         # 일단 root노드를 모르는 상태라고 해두고
    for j in range(1, E+2):                             # 0을 뺀 노드 갯수만큼 반복
        if whtkd[j] == 0:                               # whtkd[j] 노드j의 조상이 부모가 없다면,
            root = j                                    # 노드j가 루트노드
            break                                       # for문 빠져나와서

    def preorder(root):                                 # 이진 탐색을 정의해보자
            if root > 0:                                #
                print(root, end=' ')                    # 탐색한 순서를 출력하고(방문하고)
                preorder(left[root])                    # 왼쪽 노드를 순회
                preorder(right[root])                   # 오른쪽 노드를 순회

    preorder(R)                                         # 원하는 노드를 입력