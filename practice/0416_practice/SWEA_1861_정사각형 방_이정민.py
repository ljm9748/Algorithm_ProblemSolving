dx=[0,-1,0,1]
dy=[1,0,-1,0]
def DFS(x,y,cnt,now,st):
    global answer, start
    if cnt+N*N-now<answer:
        return
    else:
        flag=True
        for k in range(4):
            newx=x+dx[k]
            newy=y+dy[k]
            if 0<=newx<N and 0<=newy<N and board[newx][newy]==now+1:
                DFS(newx,newy,cnt+1,now+1,st)
                flag=False
        if flag:
            if answer<cnt:
                start=st
                answer=cnt
            elif answer == cnt:
                start=min(st,start)
            else:
                return


for tc in range(int(input())):
    N= int(input())
    board=[list(map(int, input().split())) for _ in range(N)]
    answer=0
    start=N*N+1
    for i in range(N):
        for j in range(N):
            DFS(i,j,1,board[i][j],board[i][j])
    print('#{} {} {}'.format(tc+1,start,answer))