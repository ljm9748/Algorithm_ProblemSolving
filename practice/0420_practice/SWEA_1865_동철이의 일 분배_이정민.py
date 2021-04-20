def go(idx, can):
    global answer
    # print(can)
    if can<answer:
        return
    if idx==N:
        # print(round(float(can*100),6))
        answer=max(answer, can)
        return
    else:
        for i in range(N):
            if not visited[i] and board[idx][i] !=0:
                visited[i]=True
                go(idx+1, can*board[idx][i]*0.01)
                visited[i]=False
for tc in range(int(input())):
    # print(round(0.123456667,5))
    N=int(input())
    board=[list(map(int, input().split())) for _ in range(N)]
    visited=[False]*N
    answer=0
    for i in range(N):
        visited[i]=True
        go(1, board[0][i]*0.01)
        visited[i]=False
    answer*=100
    print('#{} '.format(tc+1),end='')
    print('%.6f'%answer)
