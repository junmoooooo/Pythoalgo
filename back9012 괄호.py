import sys
input = sys.stdin.readline

from collections import deque

for _ in range(int(input())):
    brackets = input().rstrip()
    stack = deque()

    for bracket in brackets:                # 괄호를 하나씩 뽑아,
        if bracket == '(':                  # 여는 괄호라면,
            stack.append(bracket)           # 스택에 산입
            # 앞에서 부터 확인해서 여는괄호면 스택에 go
        elif stack:                         # 닫는 괄호 + 스택이 비지 않았다면,
            stack.pop()                     # 여는 괄호 스택에서 pop
            # 닫는 괄호가 나오면 여는 괄호를 빼줘~
        else:                               # 닫는 괄호인데, 스택이 비었다면, VPS 불가
                                            # 닫는 괄호 and 스택이 비어있다.
            stack = True                    # stack에 True를 할당하고 // 이거를 해주는 이유를 잘 모르겠다...?
            break                           # vps가 아니라면 뒤에는 볼 필요가 없다. break
                                            # break를 넣지 않으면 런타임 에러

    print("YES" if not stack else "NO")     # 스택에 괄호가 남아있다면 VPS가 아님

# if문이 왔다갔다하니까 알다가도 모르겠네..

    