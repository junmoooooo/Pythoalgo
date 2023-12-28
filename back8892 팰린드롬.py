# #팰린드롬   거꾸로 읽어도 똑같은 문자? 회문


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

#
#
# import sys
# input = sys.stdin.readline
#
# for tc in range(int(input())):
#     k = int(input())
#     words = [input().rstrip() for _ in range(k)]    # 주어진 단어들 입력
#
#     for i in range(k):                              # 2중 for문을 통해 모든 경우 탐색
#         for j in range(k):
#             if i == j:                              # 같은 단어를 뽑는 경우는 pass(continue)
#                 continue
#
#             word = words[i] + words[j]              # 두 단어를 뽑아 붙이기
#
#             if word == word[::-1]:                  # 회문이라면,
#                 print(word)                         # 출력하고
#                 exit(0)                             # 프로그램 종료(하나만 찾아도 되므로)
#
#     print(0)                                        # 끝까지 못찾았다면 0 출력