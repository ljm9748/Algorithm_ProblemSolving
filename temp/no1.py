dx=[1,1,-1,-1]
dy=[1,-1,1,-1]

for tc in range(int(input())):
    # 입력 형식에 맞춰 입력받기
    N,M=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(N)]
    answer=0

    for m in range(M):
        # 각 폭탄에 따른 변화조사
        ix,iy,power=map(int, input().split())
        answer+=board[ix][iy]
        board[ix][iy]=0

        # 4뱡향 확인
        for k in range(4):
            newx = ix
            newy = iy
            # power만큼 확인
            for i in range(power):
                newx += dx[k]
                newy += dy[k]
                if 0<=newx<N and 0<=newy<N:
                    answer += board[newx][newy]
                    board[newx][newy]=0             # 중복측정 방지를 위해 0으로 바꾸기
    print('#{} {}'.format(tc+1, answer))