import sys
input = sys.stdin.readline

from collections import deque
from heapq import heappush, heappop

# N = int(input())

# cnt = 0

# lectures = deque(sorted(list(tuple(map(int, input().split())) for _ in range(N)), key=lambda x : (x[0], x[1])))
# heap = []
# heappush(heap, lectures.popleft()[1])

# while lectures:
#     s, e = lectures.popleft()           # 남은 강의 중 시작 시간이 가장 빠른 강의를 꺼내고

#     standard = heappop(heap)            # 기준은 집어넣은 강의 가운데 가장 빨리 끝나는 시간

#     if s < standard:                    # 해당 강의실에 못 넣으면
#         heappush(heap, standard)        # 다시 넣고
#         heappush(heap, e)               # 새 강의실 개설

#     else:                               # 해당 강의실에 넣을 수 있으면
#         heappush(heap, e)               # 넣고 기준 갱신

# print(len(heap))                        # 정답은 힙큐의 길이(새 강의실이 생길때마다 힙큐의 길이가 늘어남)

