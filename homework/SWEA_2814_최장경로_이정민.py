def search(v, distance):
    global answer
    if answer<distance:
        answer = distance
    for i in board[v]:
        if not visited[i]:
            visited[i]=True
            search(i, distance+1)
            visited[i]=False
for tc in range(int(input())):
    N,M=map(int, input().split())
    answer=1
    board=[[] for _ in range(N+1)]
    visited=[False]*(N+1)
    for i in range(M):
        v1,v2= map(int, input().split())
        board[v1].append(v2)
        board[v2].append(v1)
    for i in range(1,N+1):
        visited[i]=True
        search(i, 1)
        visited[i]=False
    print('#{} {}'.format(tc+1, answer))