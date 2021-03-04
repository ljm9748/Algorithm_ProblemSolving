# 우 하 좌 상
dx=[0,-1,0,1]
dy=[1,0,-1,0]

def DFS(x,y,cnt):
    global answer
    for k in range(4):  # 4방향으로 보내기
        newx=x+dx[k]
        newy=y+dy[k]
        if 0<=newx<N and 0<=newy<N: # 미로판 벗어나지 않으면
            if my_map[newx][newy]==3:   # 도착
                answer=cnt
                return
            elif my_map[newx][newy]==0: # 길 위에 있으면
                my_map[newx][newy]=1
                DFS(newx,newy,cnt+1)

for tc in range(int(input())):
    answer=0    # 몇칸 갔는지
    N= int(input())
    my_map=[list(map(int,list(input()))) for i in range(N)]

    # 시작점 찾기
    for my in range(N):
        if 2 in my_map[my]:
            x=my
            y=my_map[my].index(2)
            break

    my_map[x][y]=1
    DFS(x,y,0)
    print('#{} {}'.format(tc+1, answer))