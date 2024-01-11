N = int(input())

def vlqhskcl(num):
    i = 0
    if num >= 2:
        i = vlqhskcl(num-2) + vlqhskcl(num-1)
        return i
    if num == 1:
        return 1

    if num == 0:
        return 0

print(vlqhskcl(N))