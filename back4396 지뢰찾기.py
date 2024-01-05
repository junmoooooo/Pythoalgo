import sys

input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, -1, 1, 1]  # 8방 델타 탐색
dc = [0, 0, -1, 1, -1, 1, -1, 1]  # 상 하 좌 우 좌상 우상 좌하 우하

N = int(input())

board_info = [input().rstrip() for _ in range(N)]  # 지뢰판 정보
current_status = [input().rstrip() for _ in range(N)]  # 현재 밟은 상태

ans = [(['.'] * N) for _ in range(N)]  # 정답 담을 이차원리스트
# ans = [('.'* N) for _ in range(N)]
mine = False  # 지뢰 밟았는지 여부

print(ans)

for r in range(N):
    for c in range(N):
        if current_status[r][c] == 'x':  # 밟은 곳이라면,
            cnt = 0  # 주변 지뢰 숫자 담을 변수
            for d in range(8):  # 8방 탐색
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and board_info[nr][nc] == '*':  # 해당 좌표가 범위 내에 있고 지뢰가 있다면,
                    cnt += 1  # 지뢰 숫자 추가
            ans[r][c] = str(cnt)  # 다 셌다면 정답배열에 추가(join 위해 스트링으로 형변환)

            if board_info[r][c] == '*':  # 만약 밟은 곳이 지뢰라면,
                mine = True  # 밟았다고 표시하고 넘어가기

if mine:  # 지뢰를 밟았다면
    for r in range(N):
        for c in range(N):
            if board_info[r][c] == '*':  # 모든 지뢰 위치를
                ans[r][c] = '*'  # 정답 배열에 표시

for line in ans:
    print(''.join(line))