T = int(input())

for tc in range(1, T+1):
    N = int(input())

    answer = 0
    visited = [[0] * N for _ in range(N)]       #멈출지 말지..? 


    def queens_road(r, c, erase=False):  # 어떤 (r,c) 에서 시작하면 아래, 왼쪽대각선, 오른쪽 대각선을 방문체크 해야함 erase가 ture면 지우는거?
        # 아래를 방문체크
        for x in range(r, N):
            if not erase:
                visited[x][c] += 1
            elif erase:  # 지우는 옵션이 True 라면 visited 그 depth 거는 초기화!!
                visited[x][c] -= 1

        # 아래 방향 왼쪽 대각선을 방문체크
        column_left = c
        for y in range(r, N):
            if column_left < 0 or column_left >= N:
                break
            else:
                if not erase:
                    visited[y][column_left] += 1
                elif erase:
                    visited[y][column_left] -= 1
                column_left -= 1

        # 아래 방향 오른쪽 대각선을 방문체크
        column_right = c
        for z in range(r, N):
            if column_right < 0 or column_right >= N:
                break
            else:
                if not erase:
                    visited[z][column_right] += 1
                elif erase:
                    visited[z][column_right] -= 1
                column_right += 1


    def deploy_queens(depth):  # 여기 depth 는 r c 에서의 r 과 같다고 생각
        global answer

        if depth == N:  # 이경우는 무사히 퀸들이 배치가 끝나서 최대 뎁스까지 내려간 경우
            answer += 1
            return

        else:  # 최대 뎁스까지 도달하지 못한 경우라면?
            for c in range(N):  # 각 뎁스는 N회 만큼 화살표 돌릴 기회를 가질 것.
                if visited[depth][c] == 0:
                    queens_road(depth, c)  # 아래, 대각선들 다 방문체크 하고
                    deploy_queens(depth + 1)
                    queens_road(depth, c, erase=True)  # depth 빠져나오면 방문 초기화.


    deploy_queens(0)  # 맨 위부터 시작해야함
    print('#{} {}'.format(tc, answer))


    #이것이 하나하나 푼 코드