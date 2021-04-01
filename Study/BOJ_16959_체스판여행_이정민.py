from collections import deque
# 비숍
bx=[1,1,-1,-1]
by=[-1,1,-1,1]

# 록
lx=[0,1,0,-1]
ly=[1,0,-1,0]

# 나이트
nx=[1,2,2,1,-1,-2,-2,-1]
ny=[-2,-1,1,2,2,1,-1,-2]

# 말
chess=[[bx,by], [lx,ly], [nx,ny]]

# 입력받기
N=int(input())
board=[list(map(int, input().split())) for _ in range(N)]
visited=[[[[False]*3 for _ in range(1001)] for _ in range(10)] for _ in range(10)]

deq=deque()
for i in range(3):
    deq.append([i, [0, 0], 2, 0])
    visited[0][0][2][i]=True

while len(deq)>0:
    front=deq.popleft()
    # print(front)
    if front[2] == N*N+1:
        print(front[3])
        break
    else:
        # 바꾸기
        for i in range(1,3):
            tmp=(front[0]+i)%3
            if visited[front[1][0]][front[1][1]][front[2]][tmp] == False:
                deq.append([(front[0]+i)%3, front[1], front[2], front[3]+1])
                visited[front[1][0]][front[1][1]][front[2]][tmp]=True
                # print('a:',[(front[0]+i)%3, front[1], front[2], front[3]+1])

        # 움직이기
        if front[0]==2:    # 나이트라면
            for k in range(8):
                x = front[1][0]
                y = front[1][1]
                newx = x + chess[front[0]][0][k]
                newy = y + chess[front[0]][1][k]
                if 0<=newx<N and 0<=newy<N:
                    if board[newx][newy] == front[2]:
                        if not visited[newx][newy][front[2]+1][front[0]]:
                            deq.append(([front[0], [newx, newy], front[2] + 1, front[3] + 1]))
                            # print('ap:', [front[0], [newx, newy], front[2] + 1, front[3] + 1])
                            visited[newx][newy][front[2] + 1][front[0]]=True
                    else:
                        if not visited[newx][newy][front[2]][front[0]]:
                            deq.append(([front[0], [newx, newy], front[2], front[3] + 1]))
                            # print('ap:', [front[0], [newx, newy], front[2], front[3] + 1])
                            visited[newx][newy][front[2] + 1][front[0]]=True

        else:
            # 비숍,록 움직이기
            for k in range(4):
                x = front[1][0]
                y = front[1][1]
                newx = x + chess[front[0]][0][k]
                newy = y + chess[front[0]][1][k]

                while 0<=newx<N and 0<=newy<N:
                    if board[newx][newy] == front[2]:
                        if not visited[newx][newy][front[2]+1][front[0]]:
                            deq.append(([front[0], [newx, newy], front[2]+1, front[3]+1]))
                            # print('app:',[front[0], [newx, newy], front[2] + 1, front[3] + 1])
                            visited[newx][newy][front[2] + 1][front[0]]=True
                    else:
                        if not visited[newx][newy][front[2]][front[0]]:
                            deq.append(([front[0], [newx, newy], front[2], front[3] + 1]))
                            # print('app:', [front[0], [newx, newy], front[2], front[3] + 1])
                            visited[newx][newy][front[2]][front[0]]=True
                    newx += chess[front[0]][0][k]
                    newy += chess[front[0]][1][k]
