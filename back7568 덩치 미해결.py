# 딕셔너리 덩치순위 하나 만들고나서
# { 'A' : ((55, 185), 0) } 이렇게 저장해볼까?
# 근데 비교는 어떻게해?



person = int(input())
li = {}



for i in range(1, person+1):
    w_h = list(map(int, input().split()))
    li.update( {i : [w_h,0]} )
    # print(li[i])  # value 값 불러오기 [[55, 185], 0]
    # print(li[i][0][0])
    # print(li[i][0][1])
    # print(li[i][1])
    if li[i][0][0] > 50:
        if li[i][0][1] > 180:
            li[i][1] = 1

    print(li)

# N = int(input())
# people_info = []                                    # 사람들의 키, 몸무게 정보가 담길 리스트
# rank_info = [1] * N                                 # 순위를 기록할 리스트
#
# for _ in range(N):
#     x, y = map(int, input().split())
#     people_info.append((x, y))                      # 몸무게와 키를 튜플로 리스트에 추가
#
# for now in range(N - 1):
#     now_w, now_h = people_info[now]                 # 한 명씩 뽑아서 기준(now)으로 삼고
#
#     for other in range(now + 1, N):                 # 그보다 뒤에 있는 사람들과 비교(한번씩만 비교하면 되기 때문)
#         other_w, other_h = people_info[other]
#
#         if now_w > other_w and now_h > other_h:     # 기준이 되는 사람의 덩치가 확실히 크다면,
#             rank_info[other] += 1                   # 비교되는 사람들의 순위를 1씩 증가
#
#         elif now_w < other_w and now_h < other_h:   # 비교되는 사람의 덩치가 확실히 크다면,
#             rank_info[now] += 1                     # 기준이 되는 사람의 순위를 1씩 증가
#
# print(*rank_info)                                   # 순위 정보 리스트를 unpack하여 출력

# 내가 생각한 논리는 같으나 접근 방식이 완전 다름.
#