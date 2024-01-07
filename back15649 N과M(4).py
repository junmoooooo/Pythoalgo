#
# N,M = map(int,input().split())
# arr = []
# for i in range(1, N+1):
#     arr.append(i)
# sel = [0]*M
# check = [0]*N
#
# visited = [0]
#
# def tnsdud(defs):
#     if defs == M:
#         print(*sel)
#         return
#     for i in range(N):
#         if check[i] == 0:
#             check[i] = arr[i]
#             if check[i] >= arr[defs]:
#                 sel[defs] = arr[i]
#                 tnsdud(defs+1)
#             check[i] = 0
#
# tnsdud(0)


def DFS(index):
    global N, M, nums, stack

    if len(stack) == M:
        print(*stack)
        return

    for i in range(index, N):
        stack.append(nums[i])
        DFS(i)
        stack.pop()


N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
stack = []

DFS(0)