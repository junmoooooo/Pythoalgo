# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에,
# 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.
# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
#
N = int(input())
book = {}
books =[]
for i in range(N):
    books.append(input())
    book.update({books[i]:0})
# print(book)
for j in range(len(books)):
    if books[j] in books[j]:
        book[books[j]] = book[books[j]] +1

# print(book)
# print(books)

max = 1
ans = []
for k in book:
    # print(k)
    if max < book[k] :
        max = book[k]
# print(max)
for k in book:
    if max == book[k]:
        ans.append(k)

ans = sorted(ans)
# print(ans)
print(ans[0])



# import sys
# input = sys.stdin.readline
# from collections import defaultdict
#
# books_sales_info = defaultdict(int)             # 따로 설정하지 않는 이상 value의 디폴트값은 0
#
# for _ in range(int(input())):
#     books_sales_info[input().rstrip()] += 1     # 책이 팔릴 때마다 하나씩 세고
#
# books_names = sorted(books_sales_info)          # 책 제목만 뽑아서 사전순 정렬
#
# cnt = -1
# ans = ''
#
# for book_name in books_names:                   # 책 제목을 사전순으로 뽑아서
#     if books_sales_info[book_name] > cnt:       # 현재 최대값보다 큰 경우에만(같은 경우 사전순 앞에 있는 책이 우선)
#         cnt = books_sales_info[book_name]       # 최대값 갱신
#         ans = book_name                         # 정답 갱신
#
# print(ans)


# sorted)books_sales_info.items() ,key = lanmda x:(-x[1],x[0])
# lamda는 진짜 미치겟다..


