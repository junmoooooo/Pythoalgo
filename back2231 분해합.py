#생성자의 범위 N보다 작다
#생섯자의 최솟값? N-27
# N-27 ~ N

# max(1,N-(9*len(str(N))) ~ N)
# 음수가 나올수도 있기 떄문에 max를 써줘야 된다

#N + map(int,str(N))

N= int(input())

maxtodtjdwk = max(1, N - (9* len(str(N))))
#생성자의 각 자릿수의 합의 최대치
ans = 0

for num in range(maxtodtjdwk, N+1):
    #생성자의 각 자릿수의 합의 최대치만큼 반복해야지?
    inputnum = num + sum(map(int, str(num)))
    #생성자랑 생성자 자릿수의 합
    if inputnum == N :
        ans = num
        break

print(ans)






























