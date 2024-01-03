# TC = int(input())

# def tnsduf(dep):
#     global minn

#     if dep == N:
#         a = sum(sel)
#         if a < minn:
#             minn =a
#         return
    
#     for i in range(N):
#         if chexk[i] == 0:
#             chexk[i] =1
#             sel[dep] = arr[dep][i]
#             tnsduf(dep+1)
#             chexk[i] = 0
    
# for i in range(TC):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     sel = [0]*N
#     chexk = [0]*N
#     minn = 1000
#     tnsduf(0)    # 테스트 케이스 별로 순열을 돌려야지 이자식아
#     print(f'#{i+1} {minn}')
    



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answer = 99999999999999999
    check = [0]*N

    def perm(depth, acc):
        global answer      # 글로벌을 써줘야 사용가능!

        if acc >= answer:  # 백트래킹
            return  # 이미 해당 뎁스에서 구해진 최솟값보다 크거나 같으면 의미 x

        if depth == N:  # 최후 뎁스 도달 시,
            if answer > acc:
                answer = acc  # 최솟값 갱신 시도
            return  # 아니라도 일단 리턴

        for i in range(N):
            if not check[i]:
                check[i] = 1
                perm(depth + 1, acc + nums[depth][i])
                check[i] = 0

    perm(0, 0)

    print('#{} {}'.format(tc, answer))