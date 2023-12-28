for T in range(int(input())):
    N,M = map(int,input().split())
    for Nnum in range(N):
        word = list(input().split())
        check = word[::-1]
        if word == check:
            print(word)