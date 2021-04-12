from collections import deque

# 스택 내부 연산
def stackplay(b, idx):
    global answer
    if len(stack)==0:
        stack.append([b, idx])
        return
    elif b<stack[-1][0]:
        stack.append([b,idx])
        return
    elif b==stack[-1][0]:
        stack.pop()
        stackplay(b,idx)
    else:   # 새로 들어온세 스택 탑보다 크다면 빗물계산
        tmp=stack.pop()
        if len(stack)>0:
            height=min(b, stack[-1][0])-tmp[0]
            width=idx-stack[-1][1]-1
            answer+=height*width
        # 또 계산
        stackplay(b, idx)

stack=deque()
H,W= map(int, input().split())
blocks=list(map(int, input().split()))
answer=0

# 연산 시작!!
for idx,b in enumerate(blocks):
    stackplay(b, idx)

print(answer)