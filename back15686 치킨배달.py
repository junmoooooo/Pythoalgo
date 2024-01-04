import sys
input = sys.stdin.readline

def dfs(depth, now):
    global ans

    if depth == M:                          # 살릴 M개를 뽑았다면,
        cnt = 0
        for dist_info in chicken_dists:     # 각 집별로 치킨 거리를 계산
            for dist, idx in dist_info:     # 가장 가까운 치킨집을 뽑아
                if visited[idx]:            # 해당 치킨집이 살아있다면
                    cnt += dist             # 카운팅
                    break
                if cnt > ans:               #백트래킹
                    return
        ans = min(ans, cnt)                 # 갱신하고 리턴
        return

    for i in range(now, len(chickens)):     # 현재를 기준으로 뒤로 가며
        if not visited[i]:                  # 살릴 곳은
            visited[i] = True               # 표시하고
            dfs(depth + 1, i + 1)           # 다음 depth로
            visited[i] = False              # 돌아오면 표시 풀기

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

chicken_dists = []
visited = []

# 문제 구조화   각 집별로 치킨집까지의 거리를 미리 구해 놓자!
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:             # 집이 나오면
            houses.append((r, c))       # 좌표 추가하고
            chicken_dists.append([])    # 각 집마다 치킨거리를 계산할 리트 인덱스가 집번호

        elif city[r][c] == 2:           # 치킨집이 나오면
            chickens.append((r, c))     # 좌표 추가하고
            visited.append(False)       # 폐업여부 담을 리스트

for h_i, (h_r, h_c) in enumerate(houses):           # 각 집마다
    for c_i, (c_r, c_c) in enumerate(chickens):     # 각 치킨집까지 치킨 거리를 계산해서
        chicken_dists[h_i].append((abs(h_r - c_r) + abs(h_c - c_c), c_i))
        chicken_dists[h_i].sort()                   # 치킨 거리가 가까운 순으로 정렬(정렬 통한 백트래킹)
#enumerate 인덱스와 값을 같이 뽑아줌
ans = 987654321

dfs(0, 0)
print(ans)




# import sys
# input = sys.stdin.readline
# from itertools import combinations

# N, M = map(int, input().split())

# city = [list(map(int, input().split())) for _ in range(N)]

# house = []                          # 집들의 좌표가 담길 리스트
# chicken = []                        # 치킨집의 좌표가 담길 리스트

# for r in range(N):
#     for c in range(N):
#         if city[r][c] == 1:
#             house.append((r, c))
#         elif city[r][c] == 2:
#             chicken.append((r, c))

# ans = 987654321

# for case in combinations(chicken, M):   # M개의 치킨집을 남기는 모든 경우의 수를 고려
#     cnt = 0
#     for home in house:                  # 각 집마다
#         tmp = 1000
#         for store in case:
#             tmp = min(tmp, abs(store[0] - home[0]) + abs(store[1] - home[1]))
#         cnt += tmp                      # 치킨 거리를 계산해서 더하기

#         if cnt > ans:                   # 백트래킹
#             break

#     ans = min(ans, cnt)                 # 정답 갱신

# print(ans)