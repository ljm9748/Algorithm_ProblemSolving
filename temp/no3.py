dx=[1,0,-1,0]
dy=[0,1,0,-1]
# 정보 입력 받기
for tc in range(int(input())):
    N=int(input())
    board=[list(map(int, input().split())) for _ in range(N)]

    # 로봇 위치(시작위치)찾기
    for idx in range(N):
        if 2 in board[idx]:
            x=idx
            y=board[idx].index(2)
    answer=0

    # zone이 3개이므로 3번 반복
    for i in range(3):
        # 초기 설정 후 시작
        visited=[[False]*N for _ in range(N)]
        q = []
        visited[x][y]=True
        zone_tmp=[]
        flag=-1
        q.append([x,y,0])   # 로봇의 자리 q에 넣고 시작
        while len(q)>0:
            front=q.pop(0)
            # 이미 최소방문회수가 넘어간 경우 그만가기
            if len(zone_tmp)>0 and front[2]>flag:
                break

            # zone도착한지 확인하기(3, 4, 5)
            # 최소 횟수의 범위 안에 만난 zone이 zone3인 경우 무조건 거기로 이동
            if board[front[0]][front[1]]==3:
                answer += front[2]
                board[front[0]][front[1]]=1
                x=front[0]
                y=front[1]
                break
            # 최소 횟수의 범위 안에 만난 존이 zone 4, 5인 경우 순서를 알 수 없으므로 우선 zone_tmp에 넣고 횟수 범위 설정후 계속 탐색
            elif board[front[0]][front[1]]==4:
                zone_tmp.append([4,front[0],front[1],front[2]])
                flag=front[2]
            elif board[front[0]][front[1]]==5:
                zone_tmp.append([5, front[0], front[1], front[2]])
                flag = front[2]

                # 존에 만난게 아니라면
            else:
                for k in range(4):
                    newx=front[0]+dx[k]
                    newy=front[1]+dy[k]
                    # 만약 범위를 안벗어나고, 방문하지 않았고, 벽이 아니라면
                    if 0<=newx<N and 0<=newy<N and not visited[newx][newy] and board[newx][newy] !=1:
                        visited[newx][newy]=True
                        q.append([newx, newy, front[2]+1])

        # 순회 종료 후 만약 zone이 3 이아니라 어디로 갈지 설정하지 못했다면 sort를 통해 더 앞 순서의 존으로 이동
        if flag != -1:
            zone_tmp.sort()
            board[zone_tmp[0][1]][zone_tmp[0][2]] = 1
            answer += zone_tmp[0][3]
            x=zone_tmp[0][1]
            y=zone_tmp[0][2]

    print('#{} {}'.format(tc+1, answer))
