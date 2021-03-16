import sys
input=sys.stdin.readline
# 상 우 하 좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for tc in range(int(input())):
    now=0
    answer=[0,0]
    far_list=[0,0,0,0]  # x최소, x최대, y최소, y최대

    for l in input():
        if l=='L':
            now+=3
        elif l=='R':
            now+=1
        elif l=='F':
            answer[0]+=dx[now%4]
            answer[1]+=dy[now%4]
            far_list[0]=min(answer[0],far_list[0])
            far_list[1]=max(answer[0],far_list[1])
            far_list[2]=min(answer[1],far_list[2])
            far_list[3]=max(answer[1],far_list[3])
        elif l=='B':
            answer[0] -= dx[now % 4]
            answer[1] -= dy[now % 4]
            far_list[0] = min(answer[0], far_list[0])
            far_list[1] = max(answer[0], far_list[1])
            far_list[2] = min(answer[1], far_list[2])
            far_list[3] = max(answer[1], far_list[3])

    print((far_list[1]-far_list[0])*(far_list[3]-far_list[2]))