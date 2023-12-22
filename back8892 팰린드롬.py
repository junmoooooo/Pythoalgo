# #팰린드롬   거꾸로 읽어도 똑같은 문자? 회문
#
#
# from itertools import permutations, combinations
#
# num =[1,2,3]
# perm = permutations(num,2)
# combi = combinations(num, 2)
#
# print(perm)
# print(combi)
#
# print(list(perm))
# print(list(combi))
#
# words = ['aaba', 'ba', 'ababa', 'bbaa', 'baaba']
#
# for word1, word2 in permutations(words,2):
#     p =word1 + word2
#
#     print(word1, word2, p)
#
#

import sys
input = sys.stdin.readline
from itertools import permutations, combinations

for tc in range(int(input())):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    for word1, word2 in permutations(words, 2):
        p= word1 + word2

        if p == p [::-1]:
            print(p)
            exit(0)

    print(0)




#함수처리

# def check_palindrome(w):
#     l = 0
#     r = len(w) -1
#
#     while l < r :
#         if w[l] != w[r]:
#             return False
#
#         l += 1
#         r -= 1
#
#     return w
#
# print(check_palindrome(input().rstrip()))
#
#
#여기먼저 보자
# def find():
#     global ans
#
#     for i in range(k):
#         for j in range(k):
#             if i == j:
#                 continue
#
#             p = words[i] + words[j]
#
#             if p == p[::-1]:
#                 ans =p
#                 return
#
# for tc in range(int(input())):
#     k = int(input())
#     words = [input().rstrip() for _ in range(k)]
#
#     ans = 0
#     find()
#
#     print(ans)