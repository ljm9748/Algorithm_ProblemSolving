from sys import *
import sys
setrecursionlimit(10**6)
input = sys.stdin.readline
M,N,K=map(int, input().split())
my_map=[[0]*N for i in range(M)]
visited=[[0]*N for i in range(M)]

# 우 하 좌 상
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 입력받기
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(M-y2, M-y1):
        for y in range(x1, x2):
            my_map[x][y]=1
            visited[x][y]=1

results=[]  # 각영역개수
area=101    # 101부터 영역값넣기
answer=0    # 영역별로 칸수

def DFS(x,y):
    global answer
    for k in range(4):
        newx=x+dx[k]
        newy=y+dy[k]
        if 0<=newx<M and 0<=newy<N and visited[newx][newy]==0 and my_map[newx][newy]==0:
            visited[newx][newy] = 1
            answer += 1
            DFS(newx, newy)


# 범위돌며 영역측정
for x in range(M):
    for y in range(N):
        if my_map[x][y]==0 and visited[x][y]==0:
            answer=1
            visited[x][y]=1
            DFS(x, y)
            area +=1
            results.append(answer)

results.sort()  # 오름차순
print(area-101)
for r in results:
    print(r,end=' ')

sys.exit(0)
