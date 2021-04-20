dx=[0,0,1,-1]
dy=[1,-1,-1,-1]

def queencheck(x,y):
    for k in range(4):
        newx=x+dx[k]
        newy=y+dy[k]
        while 0<=newx<N and 0<=newy<N:
            if board[newx][newy]:
                return False
            newx += dx[k]
            newy += dy[k]
    return True


def DFS(x,y):
    global answer
    if y==N-1:
        answer += 1
    else:
        for i in range(N):
            if queencheck(i, y+1):
                board[i][y+1] = True
                DFS(i, y+1)
                board[i][y+1] = False

for tc in range(int(input())):
    N=int(input())
    board=[[False]*N for _ in range(N)]
    answer=0
    for i in range(N):
        if queencheck(i,0):
            board[i][0]=True
            DFS(i,0)
            board[i][0]=False
    print('#{} {}'.format(tc+1, answer))
