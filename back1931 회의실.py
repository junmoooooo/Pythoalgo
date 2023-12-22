import sys
input = sys.stdin.readline

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort()                         # 정렬 2순위: 회의 시작 시간
meetings.sort(key=lambda x : x[1])      # 정렬 1순위: 회의 종료 시간

ans = 0
standard = -1                           # 최초 기준 설정

for s, e in meetings:                   # 시작 및 종료 시간을 꺼내서
    if s >= standard:                   # 시작 시간이 기준 시간 후라면
        ans += 1                        # 회의 시작 가능
        standard = e                    # 기준 갱신

print(ans)