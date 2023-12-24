from collections import deque

for _ in range(int(input())):
    brackets = input().rstrip()
    stack = deque()

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)

        elif stack:
            stack.pop()

        else:
            stack = True
            break

    
    print(stack)