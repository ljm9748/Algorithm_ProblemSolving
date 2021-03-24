# 우 상 좌 하
dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]

def DFS(x, y, way, cnt, line, nth):
    global max_core, min_line
    # print(core, max_core, min_line)
    # for b in board:
    #     print(*b)
    # print()
    if max_core-1>core-nth+2+cnt: # upper_bound
        return
    if nth == core+1:
        if cnt > max_core:
            max_core = cnt
            min_line = line

        elif cnt == max_core:
            min_line=min(min_line,line)
        return
    if way==4:
        newx, newy = find_core(x,y)
        for k in range(5):
            DFS(newx,newy,k,cnt,line,nth+1)
            if newx==-1 and newy==-1:
                break
    else:
        can,visit_list=can_go(x,y,way)
        if can:
            newx, newy = find_core(x, y)
            line = line+len(visit_list)
            for visit in visit_list:
                board[visit[0]][visit[1]]=2
            for k in range(5):
                DFS(newx,newy,k,cnt+1,line,nth+1)
                if newx == -1 and newy == -1:
                    break
            for visit in visit_list:
                board[visit[0]][visit[1]]=0

def find_core(x,y):
    for i in range(x,N):
        for j in range(0, N):
            if board[i][j]==1:
                if j<=y and i==x:
                    continue
                else:
                    return i,j
    return -1,-1

def can_go(x,y,way):
    visit_list=[]
    while True:
        newx=x+dx[way]
        newy=y+dy[way]
        if 0>newx or 0>newy or newx>=N or newy>=N:
            return True,visit_list
        elif board[newx][newy] == 0:
            visit_list.append([newx,newy])
            x=newx
            y=newy
        else:
            return False,visit_list

for tc in range(int(input())):
    N=int(input())
    board=[]    # 빈칸 0 core 1 방문한거 2
    core=0
    min_line=0
    max_core=0
    for n in range(N):
        board.append(list(map(int, input().split())))
        for i in range(N):
            if board[n][i] == 1:
                if n == 0 or n == N - 1:
                    board[n][i]=2
                else:
                    core += 1

    for i in range(N):
        if board[i][0]==1:
            board[i][0]=2
            core -=1
        if board[i][N-1]==1:
            board[i][N-1]=2
            core -=1

    x,y=find_core(0,-1)
    for k in range(5):
        DFS(x, y, k, 0, 0, 1)
    print('#{} {}'.format(tc+1,min_line))
