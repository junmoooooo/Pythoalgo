# tc = int(input())
# board = [list(map(int, input().split())) for _ in range(9)]


def check(board):  # 체크 함수
    for line in board:  # 이차원 리스트 내부에서 리스트를 하나씩 꺼내서
        if len(set(line)) < 9:  # 숫자가 중복되는 경우
            return 0  # 0 리턴

    return 1  # 테스트 모두 통과하면 1 리턴


for tc in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    sudoku2 = list(zip(*sudoku))  # sudoku2: 전치(열 우선)

    sudoku3 = []  # sudoku3: 칸별로

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            sudoku3.append([sudoku[i][j] for i in range(x, x + 3) for j in range(y, y + 3)])

    ans = check(sudoku) and check(sudoku2) and check(sudoku3)  # 단축평가

    print(f'#{tc} {ans}')


    