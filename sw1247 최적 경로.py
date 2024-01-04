#N개의 정점을 이어진 경로로 완전 탐색하는 문제

from collections import deque

# 두 점 사이의 맨해튼 거리를 구하는 함수
def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# dfs 탐색 코드
def dfs(now, distance, depth):                  # (현재 위치, 현재 거리, 현재 뎁스) 어떤 인자인지 잘 알아야함
    global ans

    if depth == N:                              # N개의 방문지를 모두 돌았다면
        distance += dist(house[now], end)       # 마지막 위치에서 도착지까지의 거리를 더하고
        #여태까지의 거리 에서 지금 현재 있는거리?
        ans = min(distance, ans)                # 정답 갱신
        return

    if distance > ans:                          # 중간거리가 현재 정답보다 크다면    리턴(백트래킹) 가지가 끝까지 도발 한다면
        return
    # 

    for after in range(N):                      # 다음 갈 곳 탐색 Ater는 인자
        if not check[after]:                    # 방문하지 않은 곳이라면
            check[after] = 1                    # 방문 체크하고
            dfs(after, distance+dist(house[now], house[after]), depth+1)    # 거리 및 뎁스 갱신하며 방문
            check[after] = 0                    # 나올 때는 방문 체크 해제
            

for tc in range(1, int(input())+1):
    N = int(input())
    coordinates = deque(list(map(int, input().split())))
    #좌료들을 덱에 넣고

    # 출발지, 도착지, 중간지점들 구조화
    start = [coordinates.popleft(), coordinates.popleft()]
    end = [coordinates.popleft(), coordinates.popleft()]
    house = []
    for _ in range(N):
        house.append([coordinates.popleft(), coordinates.popleft()])

    # 갱신할 정답 및 방문지 체크 배열
    ans = 987654321
    check = [0] * N

    # 모든 경우의 수 탐색
    for i in range(N):
        dfs(i, dist(start, house[i]), 0)

    print(f'#{tc} {ans}')