def Puyo(x,y,color): # 중력주기
    # 중력주기
    for j in range(6):
        for i in range(10,-1,-1):
            if puyo_map[i][j] != '.' and puyo_map[i+1][j] =='.':
                farx=12
                for k in range(i+1,12):
                    if puyo_map[k][j] !='.':
                        farx=k
                        break

                puyo_map[farx-1][j]=puyo_map[i][j]
                puyo_map[i][j]='.'



def DFS(x,y,color,bomb):    # 같은거 찾기(x,y좌표, 현재색상, 터트릴지 여부)
    global count
    if bomb:                # 터트리는 경우
        puyo_map[x][y]='.'
    for k in range(4):
        newx=x+dx[k]
        newy=y+dy[k]
        if 0<=newx<12 and 0<=newy<6 and not visited[newx][newy] and puyo_map[newx][newy]==color:
            count+=1
            visited[newx][newy]=True
            DFS(newx,newy,color,bomb)

# 우 하 좌 상
dx=[0,1,0,-1]
dy=[1,0,-1,0]
puyo_map=[]
answer=0
count=0
visited=[[False]*6 for i in range(12)]
for i in range(12):
    puyo_map.append(list(input()))

search_flag=True

while search_flag:
    visited = [[False] * 6 for i in range(12)]
    puyo_flag=False
    for x in range(12):
        for y in range(6):
            if puyo_map[x][y] != '.' and not visited[x][y]:
                visited[x][y] = True
                count = 1
                DFS(x, y, puyo_map[x][y],False)
                if count >= 4:
                    # 터뜨리기
                    visited = [[False] * 6 for i in range(12)]
                    visited[x][y] = True
                    DFS(x, y, puyo_map[x][y], True)
                    puyo_flag=True

    if puyo_flag:   # 중력주기
        Puyo(x,y,puyo_map[x][y])
        answer += 1
    else:       # 끝났다면
        search_flag=False

print(answer)


