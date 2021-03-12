import sys
input=sys.stdin.readline

# 오, 대각선, 아래
dx=[0, 1, 1]
dy=[1, 1, 0]

def DFS(x, y, way):
    global answer
    if x==N-1 and y==N-1:
        answer+=1
        return
    else:
        # 오른쪽으로 보내기
        if way==0 or way==1:
            if 0<=y+1<N and house[x][y+1]==0:
                DFS(x, y+1, 0)

        # 대각선으로 보내기
        if 0<=y+1<N and 0<= x+1<N and house[x][y+1]==0 and house[x+1][y] == 0 and house[x+1][y+1] == 0:
            DFS(x+1, y+1, 1)

        # 아래로 보내기
        if way==1 or way==2:
            if 0<=x+1<N and house[x+1][y]==0:
                DFS(x+1, y, 2)


N=int(input())
house=[list(map(int, input().split())) for _ in range(N)]
answer=0
DFS(0,1,0)
print(answer)