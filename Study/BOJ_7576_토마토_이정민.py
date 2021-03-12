import sys
input=sys.stdin.readline

# 우 하 좌 상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def BFS():
    global q_front,q_end
    while q_front!=q_end:
        tmp_front=my_queue[q_front]
        q_front+=1
        for k in range(4):
            newx=tmp_front[0]+dx[k]
            newy=tmp_front[1]+dy[k]

            if 0<=newx<N and 0<=newy<M and tomato_box[newx][newy]==0:
                tomato_box[newx][newy]=1
                my_queue[q_end] = [newx, newy, tmp_front[2]+1]
                q_end+=1
    return tmp_front[2]


M,N=map(int, input().split())
tomato_box=[list(map(int, input().split())) for _ in range(N)]

my_queue=['']*(N*M)
q_front=0
q_end=0
for x in range(N):
    for y in range(M):
        if tomato_box[x][y]==1:
            my_queue[q_end]=[x,y,0]
            q_end+=1

answer=BFS()

for tomato in tomato_box:
    if 0 in tomato:
        answer=-1
print(answer)