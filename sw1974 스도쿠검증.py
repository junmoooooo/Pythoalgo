# def check(board):  # 체크 함수
#     for line in board:  # 이차원 리스트 내부에서 리스트를 하나씩 꺼내서
#         if len(set(line)) < 9:  # 숫자가 중복되는 경우
#             return 0  # 0 리턴
#
#     return 1  # 테스트 모두 통과하면 1 리턴
#
#
# for tc in range(1, int(input()) + 1):
#     sudoku = [list(map(int, input().split())) for _ in range(9)]
#
#     sudoku2 = list(zip(*sudoku))  # sudoku2: 전치(열 우선)
#
#     sudoku3 = []  # sudoku3: 칸별로
#
#     for x in range(0, 9, 3):
#         for y in range(0, 9, 3):
#             sudoku3.append([sudoku[i][j] for i in range(x, x + 3) for j in range(y, y + 3)])
#             print(sudoku3)
#     ans = check(sudoku) and check(sudoku2) and check(sudoku3)  # 단축평가
#
#     print(f'#{tc} {ans}')

def check(board):  # 체크 함수
    for line in board:  # 이차원 리스트 내부에서 리스트를 하나씩 꺼내서
        if len(set(line)) < 9:  # 숫자가 중복되는 경우
            return 0  # 0 리턴

    return 1  # 테스트 모두 통과하면 1 리턴


for tc in range(1, int(input()) + 1):  # 테스트케이스를 정해줘
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 9x9 의 스도쿠배열을 받음

    sudoku2 = list(zip(*sudoku))  # sudoku2: 전치(열 우선)            # 전치... 뭐였드라.. ㅠㅠ

    sudoku3 = []  # 3x3 배열을 담을 스도쿠

    sudoku4 = []  # sudoku3: 칸별로

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):  # 0,3,6 번쨰 를 체크

            for i in range(3):
                for j in range(3):
                    sudoku3.append(sudoku[x + i][y + j])
            sudoku4.append(sudoku3)
            sudoku3 = []
            print(sudoku4)
    ans = check(sudoku) and check(sudoku2) and check(sudoku4)  # 단축평가

    print(f'#{tc} {ans}')
