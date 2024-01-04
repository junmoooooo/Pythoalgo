#조합문제
#모음의 범위 :1~ㅣ-2
#자음의 범위 :2~ ㅣ-1

import sys
input = sys.stdin.readline
from itertools import combinations

vowel_gather = ['a', 'e', 'i', 'o', 'u']    # 모음 모음

L, C = map(int, input().split())
letters = list(input().split())

vowels = []                                 # 모음이 들어갈 리스트
consonants = []                             # 자음이 들어갈 리스트

for letter in letters:                      # 입력받은 글자란에
    if letter in vowel_gather:              # 모음이 있으면
        vowels.append(letter)
    else:
        consonants.append(letter)

passwords = []                              # 비밀번호 들어갈 리스트

for v in range(1, L - 1):                   # 모음(v)은 최소 1개, 최대 L-2개
    for vowel in combinations(vowels, v):   # 모음에서 v개 뽑고
        for consonant in combinations(consonants, L - v):   # 자음에서 L-v개 뽑아서
            tmp_password = sorted(list(vowel + consonant))  # 더해서 정렬하기
            passwords.append(tmp_password)                  # 비밀번호 리스트에 추가

passwords.sort()                            # 비밀번호 리스트 정렬

for password in passwords:
    print(''.join(password))


#combinations(vowels, v) = vowels C v