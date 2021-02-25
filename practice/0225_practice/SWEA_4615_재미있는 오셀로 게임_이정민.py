T=int(input())
# 우, 하, 좌, 상, 대각선 아래 2개, 대각선 위 2개
dx=[0,1,0,-1,1,1,-1,-1]
dy=[1,0,-1,0,1,-1,1,-1]

for tc in range(T):
    # 기본세팅
    N,M= map(int, input().split())
    board=[[0]*N for _ in range(N)]
    board[N//2][N//2]=board[N//2-1][N//2-1]=2
    board[N//2-1][N//2]=board[N//2][N//2-1]=1

    # 지금과 다른 내 돌이 있는 위치를 찾는함수
    def findplace(x,y,dir,color):
        tmp_farx=newx=x
        tmp_fary=newy=y
        while board[newx][newy] !=0:    # 사이에만 존재해야하기때문에 0만나기 전까지
            if board[newx][newy]==color and (newx!=x or newy !=y):  # 새로 놓은 돌이 아닌 새로운 같은 색의 돌을 만나면
                tmp_farx=newx
                tmp_fary=newy
                break
            if 0 <= newx + dx[dir] < N and 0 <= newy + dy[dir] < N: # 범위내부에 있으면 그 방향으로 이동
                newx=newx + dx[dir]
                newy=newy + dy[dir]
            else:   # 범위를 넘으면 끝내기
                break
        return tmp_farx,tmp_fary

    for i in range(M):
        # 돌놓는 위치 입력, 놓기
        y,x,color=map(int, input().split())
        x-=1
        y-=1
        board[x][y]=color

        for j in range(8):  # 8방향 확인하기
            farx,fary=findplace(x,y,j,color)
            newx=x
            newy=y
            # 함수를 통해 얻은 위치까지 다 바꾸기
            while newx!=farx or newy != fary:
                board[newx][newy]=color
                newx+=dx[j]
                newy+=dy[j]



    white=black=0
    # 돌 개수 count
    for b in board:
        white += b.count(2)
        black += b.count(1)


    print('#{} {} {}'.format(tc+1, black, white))


