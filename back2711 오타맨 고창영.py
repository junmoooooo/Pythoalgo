# TC = int(input())
#
# for i in range(TC):
#
#     word = list(input())
#     er = int(word[0])
#     아니 이러면 내가 10의자리숫자가 넘어가버리면 오류가 나잔아
#     word[er+1:er+2] = []
#     word[0:2] = []
#     print("".join(word))
#


for _ in range(int(input())):
    index, word = input().split()                # 타겟 인덱스와 문자열을 입력받아 할당
    # 근데 솔직히 이거는 너무한거 아니냐고
    index = int(index)                           # 인덱스를 정수로 형변환

    print(word[:index - 1] + word[index:])       # 타겟 인덱스를 기준으로 문자열을 앞뒤로 슬라이싱하여 이어붙인 후 출력