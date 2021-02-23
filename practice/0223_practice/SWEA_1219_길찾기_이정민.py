# 전체 tc
T= 10

for tc in range(T):
    testcase, edge = map(int, input().split())  # tc수, 간선수
    road_list=list(map(int, input().split()))
    vertexes = {}  # 정점, 간선간의 관계 나타낼 딕셔너리
    visited = [False]*100  # 방문여부
    answer = 0


    def DFS(now):
        global visited, answer
        visited[now] = True
        if vertexes.get(now) is not None:
            for near in vertexes.get(now):  # 인접 정점 확인
                if  visited[near] == False:  # 방문아직 안했다면
                    if near == 99:
                        answer = 1
                        return
                    DFS(near)


    # 정점간의 관계 입력
    for i in range(edge):
        N=road_list[2*i]
        M=road_list[2*i+1]
        # 딕셔너리에 없으면 새로 만들고 이미 key 있으면 추가
        if vertexes.get(N) is None:
            vertexes[N] = [M]
        else:
            vertexes[N].append(M)

    # 첫번째 정점 순회하며 시작
    DFS(0)

    #print(vertexes)
    print('#{} {}'.format(tc+1, answer))
