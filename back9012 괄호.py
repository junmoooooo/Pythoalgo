import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    brackets = input().rstrip()
    stack = deque()

    for bracket in brackets:                # 괄호를 하나씩 뽑아,
        if bracket == '(':                  # 여는 괄호라면,
            stack.append(bracket)           # 스택에 산입
        
        elif stack:                         # 닫는 괄호 + 스택이 비지 않았다면,
            stack.pop()                     # 여는 괄호 스택에서 pop

        else:                               # 닫는 괄호인데 스택이 비었다면, VPS 불가
            stack = True                    # stack에 True를 할당하고
            break                           # break

    print("YES" if not stack else "NO")     # 스택에 괄호가 남아있다면 VPS가 아님