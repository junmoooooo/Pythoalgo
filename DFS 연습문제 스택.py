dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
vilige = [list(map(int,input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if vilige[i][j] == 1:
            cnt = 1
            stack = []
            stack.append((i,j))

            while stack:
                vilige[i][j] = 0
                print(*vilige)

                r, c = stack.pop()

                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]

                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if vilige[nr][nc] == 0:
                        continue
                    stack.append((nr,nc))
                    vilige[nr][nc] = 0
                    cnt += 1
                    print(cnt)
            print(cnt)


print(*vilige)