# tc개수
T= int(input())

dx=[0,1,0,-1]
dy=[1,0,-1,0]
for tc in range(T):
    my_map=[]
    N= int(input())
    for _ in range(N):
        my_map.append([0]*N)

    k=0
    num=0
    nowx=0
    nowy=-1

    for i in range(N*2, 0, -1): # 전체 움직이는 변의 횟수
        for j in range(i//2):   # 한변에서 움직이는 횟수
            num+=1
            nowx += dx[k % 4]
            nowy += dy[k % 4]
            my_map[nowx][nowy]=num
        k+=1

    print('#{}'.format(tc+1))
    for i in range(N):
        print(*my_map[i])



