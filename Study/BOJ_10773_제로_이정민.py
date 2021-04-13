from collections import deque
stack=deque()
for i in range(int(input())):
    tmp=int(input())
    if tmp == 0:
        stack.pop()
    else:
        stack.append(tmp)
print(sum(stack))