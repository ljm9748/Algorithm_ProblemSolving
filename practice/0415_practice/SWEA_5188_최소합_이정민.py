for tc in range(int(input())):
    N= int(input())
    inpboard=[list(map(int, input().split())) for _ in range(N)]
    board=[[650]*N for _ in range(N)]
    board[0][0]=inpboard[0][0]
    # 첫 세모
    for i in range(N):
        for j in range(i+1):
            if 0<=j+1<N and 0<=i-j<N:
                board[j+1][i-j]=min(board[j][i-j]+inpboard[j+1][i-j], board[j+1][i-j])
            if 0<=j<N and 0<=i-j+1<N:
                board[j][i-j+1]=min(board[j][i-j]+inpboard[j][i-j+1], board[j][i-j+1])
    # 두번째 세모
    for i in range(N, 2*N-1):
        for j in range(1,N):
            if 0<=j+1<N and 0<=i-j<N:
                # board[j][i-j]
                board[j+1][i-j]=min(board[j][i-j]+inpboard[j+1][i-j], board[j+1][i-j])
            if 0<=j<N and 0<=i-j+1<N:
                board[j][i-j+1]=min(board[j][i-j]+inpboard[j][i-j+1], board[j][i-j+1])
    print('#{} {}'.format(tc+1, board[N-1][N-1]))