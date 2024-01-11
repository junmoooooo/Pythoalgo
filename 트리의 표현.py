# 5 4
# 2 1, 2 4, 4 3, 4 5    >> 부모, 자식
# 그림을 그려보자
V, E = map(int, input().split())
edges = list(map(int, input().split()))

left = [0] * (V+1)          # 자식을 이용해서
right = [0] * (V+1)         # 부모를??
ancestors = [0] * (V+1)     # 조상 

for i in range(E):
    parent, child = edges[i*2], edges[i*2+1]
    if not left[parent]:      
        left[parent] = child
        # 부모를 기준으로 자식을 정하기
    else:
        right[parent] = child
        # 자식을 기준으로 부모를 정하기?
        
    ancestors[child] = parent


# print(left, right)
# print(ancestors)

root = None
for j in range(1, V+1):
    if ancestors[j] == 0:
        root = j
        break

def preorder(node):
    if node > 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])

def inorder(node):
    if node > 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])

def postorder(node):
    if node > 0:
        postorder(left[node])
        postorder(right[node])
        print(node, end=' ')

preorder(root)
print()
inorder(root)
print()
postorder(root)