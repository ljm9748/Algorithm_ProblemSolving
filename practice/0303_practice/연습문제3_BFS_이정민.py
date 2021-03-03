# 리스트큐
class ListQueue:
    def __init__(self):
        self.queue=[]

    def enQueue(self,A):
        self.queue.append(A)

    def deQueue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False

    def Qpeek(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            return self.queue[0]

# 순회
def BFS(my_queue):
    while not my_queue.isEmpty():
        vert=my_queue.deQueue()
        print(vert)
        for v in vertexes.get(vert):
            if not visited[v]:
                my_queue.enQueue(v)
                visited[v]=True


# 그래프 입력
vertex, edge=map(int,input().split())

# visited,vertexes 초기화
visited=[False]*(vertex+1)
vertexes={}

# 정점간의 관계 입력
for i in range(edge):
    N,M= map(int, input().split())
    # 딕셔너리에 없으면 새로 만들고 이미 key 있으면 추가
    if vertexes.get(N) is None:
        vertexes[N]=[M]
    else:
        vertexes[N].append(M)

    if vertexes.get(M) is None:
        vertexes[M]=[N]
    else:
        vertexes[M].append(N)

# 초기설정
my_queue=ListQueue()
my_queue.enQueue(1)
visited[1]=True
BFS(my_queue)