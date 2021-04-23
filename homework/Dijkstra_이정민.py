import heapq
# 노드, 간선수 입력받기
N,M=map(int, input().split())
board={}
visited=[False]*N
distance=[987654321]*N
myq=[]

# 그래프 입력받기
# start, end, far
for i in range(M):
    start, end, far= input().split()
    far=int(far)
    if board.get(start) is None:
        board[start]=[[end, far],]
    else:
        board[start].append([end,far])

# 시작노드 입력받기
startnode=input()
distance[ord(startnode)-ord('a')]=0
heapq.heappush(myq, [0, startnode])
visited[ord(startnode)-ord('a')]=True
while False in visited and len(myq) >0:
    front=heapq.heappop(myq)

