import sys
input = sys.stdin.readline

N = int(input())
ans = 0

check_vertical = [False] * N                            # 상하 체크
check_diagonal_left = [False] * (2 * N - 1)             # 왼쪽 대각선 체크
check_diagonal_right = [False] * (2 * N - 1)            # 오른쪽 대각선 체크

def n_queen(depth):
    global ans

    if depth == N:                                      # 기저 사례: depth가 N까지 도달하면 성공!
        ans += 1                                        # 정답에 1 추가하고 리턴
        return

    for i in range(N):                                  # 해당 depth에서 하나씩 둬보며
        if check_vertical[i] or check_diagonal_left[depth - i] or check_diagonal_right[depth + i]:
            continue                                    # 상하 or 왼쪽 대각선 or 오른쪽 대각선에 퀸이 있다면 패스

        check_vertical[i] = True                        # 없다면 각각 체크하고
        check_diagonal_left[depth - i] = True
        check_diagonal_right[depth + i] = True

        n_queen(depth + 1)                              # 다음 depth로 이동

        check_vertical[i] = False                       # depth에서 나올 때 체크 풀어주기(중요)
        check_diagonal_left[depth - i] = False
        check_diagonal_right[depth + i] = False

n_queen(0)                                              # 항상 0번 depth에서 시작

print(ans)