#생성자의 범위 N보다 작다
#생섯자의 최솟값? N-27
# N-27 ~ N

# max(1,N-(9*len(str(N))) ~ N)
# 음수가 나올수도 있기 떄문에 max를 써줘야 된다

#N + map(int,str(N))


import sys
input = sys.stdin.readline

N= int(input())

start = max(1, N - (9* len(str(N))))
ans = 0

for num in range(start, N+1):
    disaassemble_sum = num + sum(map(int, str(num)))

    if disaassemble_sum == N :
        ans = num
        break

print(ans)