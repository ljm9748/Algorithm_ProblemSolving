def go(now, tmpsum):
    global answer
    if tmpsum>=answer:
        return
    if False not in visited:
        answer=min(answer, tmpsum+board[now][0])
        return
    else:
        for i in range(1,N):
            if i != now and not visited[i]:
                visited[i]=True
                go(i, tmpsum+board[now][i])
                visited[i]=False


for tc in range(int(input())):
    N= int(input())
    board=[list(map(int, input().split())) for _ in range(N)]
    visited=[False]*(N)
    visited[0]=True
    answer=100*100
    go(0,0)
    print('#{} {}'.format(tc+1, answer))