# panlist = input().split()           #현재 회원리스트


pnalist = ['muzi', 'frodo', 'apeach', 'neo']
singolist2 = [('muzi','frodo'),('apeach','frodo'), ('frodo','neo'), ('muzi','neo'), ('apeach','muzi')]
k= int(input())
print(pnalist)
print(pnalist[0])

print(singolist2)
print(singolist2[0][1])

num =0

singo ={}
for i in range(len(pnalist)):
    singo.update({pnalist[i]:0})

for i in range(len(singolist2)):
    for j in range(len(pnalist)):
        if singolist2[i][0] == pnalist[j]:
            num = singo.get(pnalist[j])
            num += 1
            singo.update({pnalist[j]:num})
print(singo)


# 회원목록 받고
# 누가 누굴 신고 했는지 신고리스트 받은다음에
# 신고리스트 만큼 체크??
# 만약 신고리스트[i][0]에서 [0]의 값이 회원목록[0]과 같다면,
# 딕셔너리 신고리스트에 신고당한 사람의 v값을 +1
# 

  @override
  late _MyHomePageState createState() => _MyHomePageState();
}
