import sys
input = sys.stdin.readline

def preorder(now):              # 전위 순회   
    print(now, end = '')        # 루트부터 찍고
    if tree[now][0] != '.':
        preorder(tree[now][0])  # 왼쪽 자식 찍고
    if tree[now][1] != '.':
        preorder(tree[now][1])  # 오른쪽 자식 찍고

def inorder(now):               # 중위 순회
    if tree[now][0] != '.':
        inorder(tree[now][0])   # 왼쪽 자식부터 찍고
    print(now, end = '')        # 루트 찍고
    if tree[now][1] != '.':
        inorder(tree[now][1])   # 오른쪽 자식 찍고

def postorder(now):             # 후위 순회
    if tree[now][0] != '.':
        postorder(tree[now][0]) # 왼쪽 자식부터 찍고
    if tree[now][1] != '.':
        postorder(tree[now][1]) # 오른쪽 자식 찍고
    print(now, end = '')        # 루트 찍고

V = int(input())
tree = dict()                   # 딕셔너리 형태로 트리 표현

for _ in range(V):
    parent, L, R = input().split()
    tree[parent] = [L, R]

preorder('A')
print('')
inorder('A')
print('')
postorder('A')