def go(idx, cost, start):
    global answer
    if cost>answer:
        return
    if False not in visited:
        if board[idx][start]==0:
            return
        answer=min(answer, cost+board[idx][start])
    else:
        for i in range(N):
            if i != idx and not visited[i] and board[idx][i] != 0:
                visited[i]=True
                go(i, cost+board[idx][i], start)
                visited[i]=False

N= int(input())
board=[list(map(int, input().split())) for _ in range(N)]
visited = [False]*N
answer=10*1000000
for i in range(N):
    visited[i]=True
    go(i,0,i)
    visited[i]=False
print(answer)