import sys
input = sys.stdin.readline
com=int(input())
edge=int(input())
vertexes={}
answer=0
visited=[False]*(com+1)


def DFS(now):
    global visited, answer
    visited[now] = True
    if vertexes.get(now) is not None:
        for near in vertexes.get(now):  # 인접 정점 확인
            if visited[near] == False:  # 방문아직 안했다면
                answer+=1   # 감염 추가
                DFS(near)

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

DFS(1)
print(answer)