def find(P, N):
    l, r = 1, P                                     # 좌우 기준 설정
    c = int((l + r) / 2)                            # 최초 중간 좌표(펼친 곳)
    cnt = 0

    while c != N:                                   # 목표 페이지 찾을 때까지

        if c > N:                                   # 펼친 곳이 목표 페이지보다 뒤면
            r = c                                   # 펼친 곳을 새로운 오른쪽 기준으로 삼고
            c = int((l + r) / 2)                    # 다시 중간을 펼친다

        elif c < N:                                 # 펼친 곳이 목표 페이지보다 앞이면
            l = c                                   # 펼친 곳을 새로운 왼쪽 기준으로 삼고
            c = int((l + r) / 2)                    # 다시 중간을 펼친다

        cnt += 1

    return cnt                                      # 총 펼친 횟수를 리턴한다

for tc in range(1, int(input()) + 1):
    p, a, b = map(int, input().split())

    A = find(p, a)
    B = find(p, b)
    ans = 0 if A == B else 'A' if A < B else 'B'    # 삼항 연산자 통한 정답 표현

    print(f'#{tc} {ans}')

    # ans = 0 if A == B  | else 'A' if A < B | else 'B'  # 삼항 연산자 통한 정답 표현