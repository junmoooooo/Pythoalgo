TC = int(input())
now=0
ans=0

for _ in range(TC):
    now = 0
    ans = 0
    OX = list(input())
    for i in range(len(OX)+1):
        OX.append("X")
        if OX[i] == "O":
            now = now +1
            ans = ans + now
        else:
            now = 0
    print(ans)


#
# for _ in range(int(input())):
#     results = input().rstrip()
#     ans = 0
#     cnt = 0
#
#     for result in results:
#       문자도 가능하다고!!!!!
#         if result == 'O':   # 맞았으면
#             cnt += 1        # 누적치 +1
#             ans += cnt      # 정답에 현재 누적치 더해주기
#
#         elif result == 'X': # 틀렸으면
#             cnt = 0         # 누적치 초기화
#
#     print(ans)