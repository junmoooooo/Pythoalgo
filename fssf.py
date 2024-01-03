# for T in range(int(input())):
#     N,M = map(int,input().split())
#     for Nnum in range(N):
#         word = list(input().split())
#         check = word[::-1]
#         if word == check:
#             print(word)


arr = list(map(int,input().split()))
sel = [0]*len(arr)
check = [0]*len(arr)

def tnsdud(defs):
    if defs == len(arr):
        print(sel)
        return
    for i in range(len(arr)):
        if check[i] == 0:
            check[i] = 1
            sel[defs] = arr[i]
            tnsdud(defs+1)
            check[i] = 0

tnsdud(0)
