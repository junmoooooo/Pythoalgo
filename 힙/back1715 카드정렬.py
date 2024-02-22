from collections import deque
from heapq import heappush, heappop, heapify


N = int(input())
card =deque()
for _ in range(N):
    card.append(int(input()))

# for _ in range(N):
# heappush(card, int(input())) 
# heapify(card) 도 시간복잡도를 잡아 먹어버리기 때문에
ans = 0


heapify(card)

while len(card) > 1:
    card1, card2 = heappop(card), heappop(card)
    tmp = card1 + card2

    ans =+ tmp

    heappush(card, tmp)    

print(ans)