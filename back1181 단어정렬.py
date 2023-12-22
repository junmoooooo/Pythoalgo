import sys
input = sys.stdin.readline

N = int(input())

words = [input().rstrip() for _ in range(N)]
#input받는다 N번

words = list(set(words))
words.sort()
words.sort(key = lambda x : len(x))

# words.sort(key = lambda x : (len(x), x))

for word in words :
    print(word)