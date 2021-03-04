# 순회
def BFS():
    global answer
    while len(my_queue) != 0:   # 큐가 비기 전까지
        vert = my_queue.pop(0)
        for v in vertexes.get(vert[0]):     # 맨 앞의 노드 인접노드들중 아직 탐색 안한노드 큐에 넣기
            if v==G:                        # 정답찾으면 return
                answer= vert[1]+1
                return
            if not visited[v]:
                my_queue.append([v, vert[1]+1])
                visited[v]=True


for tc in range(int(input())):
    vertex,edge=map(int,input().split())
    vertexes={}
    visited=[False]*(vertex+1)
    # 정점간의 관계 입력
    for i in range(edge):
        N, M = map(int, input().split())
        # 딕셔너리에 없으면 새로 만들고 이미 key 있으면 추가
        if vertexes.get(N) is None:
            vertexes[N] = [M]
        else:
            vertexes[N].append(M)

        if vertexes.get(M) is None:
            vertexes[M] = [N]
        else:
            vertexes[M].append(N)
    S,G=map(int, input().split())
    my_queue=[]
    my_queue.append([S,0])
    visited[S]=True
    answer=0
    BFS()
    print('#{} {}'.format(tc+1,answer))
