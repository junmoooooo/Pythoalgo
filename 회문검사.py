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



#투포인트 알고리즘

# word = input('단어를 입력하세요 :')
#
# left = 0    # 시작 인덱스
# right = len(word)-1 #마지막 인덱스
# is_palindrome =True
# while left < right:
#     if word[left] == word[right]:
#         left +=1
#         right -= 1
#         continue
#     else:
#         is_palindrome = False
#         break
#
# print(is_palindrome)


# lexicofraphoc sort


#문자열 찾기
t ='hello world'
p = 'wor'

def find_word(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break
        if cnt == M:
            return i
    return '못찾았음'

print(find_word(p,  t))