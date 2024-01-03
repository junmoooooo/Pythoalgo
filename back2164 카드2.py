from collections import deque

cards = deque()
for num in range(1, int(input())+1):
    cards.append(num)

while len(cards) >1:
    cards.popleft()
    cards.append(cards.popleft())
    # 카드의 맨앞을 뽑아서 맨뒤로 보내주라!
print(cards[0])


