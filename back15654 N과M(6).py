# 정점이 N개인 유방향 비순환 그래프를  M번 깊이까지 DFS탐색 할 수 있는 경우의 수
# 조합이 필요 이전 depth에서 다 검토를 하였기에

import sys
input = sys.stdin.readline

def combination(depth, idx):

    if depth == M:
        print(*ans)
        return

    for i in range(idx, N):  # 요부분이 제일 중요함
        if not check[i]:
            check[i] = 1
            ans[depth] = nums[i]
            combination(depth + 1, i + 1)
            check[i] = 0

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

check = [0] * N
ans = [0] * M

combination(0, 0)