from collections import deque
import sys
input= sys.stdin.readline
N= int(input())
q=deque()
for i in range(N):
    line=input()
    myl=line.split()

    if myl[0]=='push':
        q.append(myl[1].strip())
    elif myl[0] == 'pop':
        if len(q)==0:
            print(-1)
        else:
            tmp=q.popleft()
            print(tmp)
    elif myl[0] == 'size':
        print(len(q))
    elif myl[0] == 'empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif myl[0] == 'front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])