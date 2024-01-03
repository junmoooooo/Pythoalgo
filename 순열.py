# arr = ['A', 'B', 'C']

                
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i != j and j != k and k != i:
#                 print([arr[i], arr[j], arr[k]])

# 백트래킹 => 가지치기
# for문을 다 돌고 나서 if문을 돌아버리면 효율이 너무 떨어짐
# 여기서 가지치기를 한다 면 for문이 한번 돌때 조건이 맞지 않으면 빠르게 처리
#

arr = ['A', 'B', 'C', 'D']  # 재료 리스트
sel = [0, 0, 0, 0]  # 재료뽑기 selection
check = [0, 0, 0, 0]  # 뽑을지 말지 결정하는 리스트


def perm(depth):  # 각자 뎁스에서는? 
    if depth == 4:  # 최고 뎁스에 도달했으면? # if depth == len(sel)
        print(sel)  # print
        return

    for i in range(4):  # 3번의 화살표 떨어트릴 기회
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?               check가 0이면 sel을 사용할수가 잇다는거.. i가 기둥??
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고    
            sel[depth] = arr[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1)
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)

perm(0)