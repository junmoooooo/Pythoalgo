T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    answer = 0

    def deploy_queens(current_depth):
        global answer
        if current_depth == N:
            answer += 1
            return

        for i in range(N):
            arr[current_depth] = i
            for check_depth in range(current_depth):
                if arr[check_depth] == arr[current_depth]:  # 열 검사부터
                    break
                if (current_depth - check_depth) == abs(arr[current_depth] - arr[check_depth]):  # 대각선 검사 행의 차이와 열의 차이가 같아 버리면
                    break
            else:
                deploy_queens(current_depth+1)

    deploy_queens(0)
    print('#{} {}'.format(tc, answer))