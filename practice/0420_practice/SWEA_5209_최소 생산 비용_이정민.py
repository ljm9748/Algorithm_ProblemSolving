def DFS(idx, cost):
    global answer
    if idx==N:
        answer = min(answer, cost)
    if cost>=answer:
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i]=True
                DFS(idx+1, cost+board[idx][i])
                visited[i]=False

for tc in range(int(input())):
    N=int(input())
    board=[list(map(int, input().split())) for _ in range(N)]
    visited=[False]*N
    answer=100*N
    for i in range(N):
        visited[i]=True
        DFS(1, board[0][i])
        visited[i]=False
    print('#{} {}'.format(tc+1, answer))
