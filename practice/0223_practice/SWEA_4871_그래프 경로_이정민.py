# 전체 tc
T= int(input())

for tc in range(T):
    vertex, edge = map(int, input().split())  # 정점수, 간선수
    vertexes = {}  # 정점, 간선간의 관계 나타낼 딕셔너리
    visited = [False] * (vertex + 1)  # 방문여부
    visited[0] = True  # 사용하지 않는 0번 idx
    answer = 0


    def DFS(now):
        global visited, answer
        print('function')
        visited[now] = True
        if vertexes.get(now) is not None:
            for near in vertexes.get(now):  # 인접 정점 확인
                if  visited[near] == False:  # 방문아직 안했다면
                    if near == end:
                        answer = 1
                        return
                    DFS(near)


    # 정점간의 관계 입력
    for i in range(edge):
        N, M = map(int, input().split())
        # 딕셔너리에 없으면 새로 만들고 이미 key 있으면 추가
        if vertexes.get(N) is None:
            vertexes[N] = [M]
        else:
            vertexes[N].append(M)
        print(vertexes)
    start, end= map(int, input().split())
    print(start,end)

    print(visited)
    # 첫번째 정점 순회하며 시작(만약 1부터 정점이 입력되지않을경우 list만들어서 이용)
    DFS(start)

    #print(vertexes)
    print('#{} {}'.format(tc+1, answer))
