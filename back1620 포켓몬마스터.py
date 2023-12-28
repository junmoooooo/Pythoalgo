index, quizunm = input().split()
pokedex ={}
quizs =[]
ans = []
poketmons= {}

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    # 값이 없으면 None을 반환하거나 예외 처리를 수행할 수 있습니다.
    return None

for i in range(int(index)):
    poketmon = input()
    poketmons={i:poketmon}
    pokedex.update(poketmons)

for i in range(int(quizunm)):
    quiz = input()
    quizs.append(quiz)

for j in range(len(quizs)):
    if quizs[j].isnumeric():
        # print(quizs[j])
        ans.append(pokedex.get(int(quizs[j])-1))
    else:
        ans.append(get_key_by_value(pokedex,quizs[j])+1)



# print(pokedex)
# print(quizs[0].isnumeric())
# print(quizs[0])
print(ans)
