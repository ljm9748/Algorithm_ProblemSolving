# 전체 tc
T=int(input())


def countWord(my_map, x, y, dir): # 방향, 시작점, map 주고 cnt 하는 함수
    cnt = 0
    if dir==0:  # 가로
        for i in range(y, len(my_map[0])):
            if my_map[x][i]==1:
                cnt +=1
            else:
                break
    if dir==1:  # 세로
        for i in range(x, len(my_map[0])):
            if my_map[i][y]==1:
                cnt +=1
            else:
                break
    #print(x,y,dir,cnt)
    return cnt


for tc in range(T):
    N,K=map(int,input().split())

    # 단어퍼즐 입력
    my_map=[]
    for _ in range(N):
        my_map.append(list(map(int, input().split())))

    cnt=0
    for x in range(N):
        for y in range(N):
            if my_map[x][y]==1:

                # 가로
                tmp_cnt = 0
                if y==0:
                    tmp_cnt = countWord(my_map,x,y,0)
                elif my_map[x][y-1]==0:
                    tmp_cnt = countWord(my_map,x,y,0)
                if tmp_cnt==K:
                    cnt+=1

                # 세로
                tmp_cnt = 0
                if x==0:
                    tmp_cnt = countWord(my_map,x,y,1)
                elif my_map[x-1][y]==0:
                    tmp_cnt = countWord(my_map,x,y,1)
                if tmp_cnt==K:
                    cnt+=1
    print('#{} {}'.format(tc+1, cnt))


