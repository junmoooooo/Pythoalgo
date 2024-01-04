# 정점이 N개인 무방향 완전 그래프를 M번 깊이까지 
# DFS탐색 할 수 있는 경우의수
# 


import sys
input = sys.stdin.readline

def perm(depth):

    if depth == M:                  # M번째 depth에 도달하면
        print(*ans)                 # 출력하고 리턴
        return

    for i in range(N):              # N개의 수를 모두 검토하며
        if not check[i]:            # 뽑지 않았다면
            check[i] = 1            # 뽑고
            ans[depth] = nums[i]    # 정답에 추가
            perm(depth + 1)         # 다음 depth로 이동
            check[i] = 0            # 나오면서 뽑지 않은 것으로 수정

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

check = [0] * N
ans = [0] * M

perm(0)


# def perm(dep):
#     if dep == M:
#         print(*ans)
#         return
#     for num in nums:
#         if num not in visited:
            


# N, M = map(int, input().split())

# nums = 