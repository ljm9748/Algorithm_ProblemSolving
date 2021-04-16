dx=[0,1,-1,0]
dy=[1,0,0,-1]
def DFS(num, x, y):
    if len(num)==7:
        answer.add(num)
        return
    else:
        for k in range(4):
            newx=x+dx[k]
            newy=y+dy[k]
            if 0<=newx<4 and 0<=newy<4:
                tmpnum=num+board[newx][newy]
                DFS(tmpnum,newx,newy)


for tc in range(int(input())):
    board=[list(input().split()) for _ in range(4)]
    visited=[]
    answer=set()
    for i in range(4):
        for j in range(4):
            DFS(board[i][j],i,j)
    print('#{} {}'.format(tc+1, len(answer)))