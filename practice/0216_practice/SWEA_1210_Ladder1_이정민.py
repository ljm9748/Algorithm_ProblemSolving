T=10

# 좌 우 상
dx=[0,0,-1]
dy=[-1,1,0]
for tc in range(T):
    # 입력
    input()
    ladder=[]
    for _ in range(100):
        ladder.append(list(map(int,input().split())))

    # 시작점 설정
    x=99
    y=0
    for i in range(100):
        if ladder[99][i]==2:
            y=i
            break
    # 방향에따라 이동
    k=2
    while x>0:
        #print(x,y,k)
        if k==0 or k==1:
            while 0<=y+dy[k]<=99 and ladder[x+dx[k]][y+dy[k]]==1:
                x=x+dx[k]
                y=y+dy[k]
                #print(x, y, k, k)
            k=2
            x = x + dx[k]
            y = y + dy[k]
            continue
        else:
            for i in range(0,3):
                if 0<=y+dy[i]<=99 and ladder[x + dx[i]][y + dy[i]] == 1:
                    x = x + dx[i]
                    y = y + dy[i]
                    k=i
                    break

    print('#{} {}'.format(tc+1,y))
