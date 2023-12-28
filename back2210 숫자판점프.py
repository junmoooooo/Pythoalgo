# 결국 25 * 4^5  = > 25 * 1024
# 이거진길은 DFS를 사용하여라

import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, num):                                         # 함수(좌표, 현재 숫자)
    #num = 지금까지 붙인 숫자?
    stack = deque([(r, c, num)])                            # 스택에 넣고

    while stack:                                            # 스택이 빌 때까지
        r, c, num = stack.pop()                             # 꺼내서
        if len(num) == 6:                                   # 길이가 6이라면
            cases.add(num)                                  # 케이스에 넣고
            continue                                        # 해당 위치에서는 더이상 탐색하지 않음
        # 왜 else를 안써?
        for d in range(4):                                  # 길이가 6 미만이라면 4방 탐색
            nr, nc = r + dr[d], c+ dc[d]                    # 다음 좌표에서
            if 0 <= nr < 5 and 0 <= nc < 5:                 # 숫자판 범위 내에 있다면
                stack.append((nr, nc, num + board[nr][nc])) # 해당 좌표 숫자 꼬리에 붙여서 스택에 추가

board = list(input().split() for _ in range(5))             # 숫자판 입력받기(스트링으로)

cases = set()                                               # 중복 피하기 위해 set으로 case 구성

for r in range(5):                                          # 모든 위치에서
    for c in range(5):
        #이중 for문을 돌면서 dfs를 해라.                                      
        dfs(r, c, board[r][c])                              # dfs

print(len(cases))                                           # 정답은 케이스의 길이