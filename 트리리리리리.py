V, E = map(int, input().split())
tree = list(map(int,input().split()))

left = [0] * (V+1)       # 0번의 인덱스를 버리고 노드의 갯수만큼 구하기 위해 V+1
right = [0] * (V+1)
ancestors = [0] *(V+1)

for i in range(E):
    p, c = tree[i*2], tree[i*2+1]   # 순서 없이 받은 tree의 입력값을 부모, 자식 순으로 들어가도록 나누는 작업
    if not left[p]:
        left[p] = c         # 노드가 가지는 왼쪽 자식
    else:
        right[p] = c        # 노드가 가지는 오른쪽 자식

    ancestors[c] = p        # 노드가 가지는 부모노드


    print(left, right)
    print(ancestors)
# 여기까지 트리 만들기

root = None                 # 
for j in range(1, V+1):     # 
    if ancestors[j] ==0:    # 
        root = j
        break