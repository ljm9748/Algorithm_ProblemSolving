import heapq
def dijkstra(now, far):
    myq=[]
    distance = [10000000] * (N + 1)
    heapq.heappush(myq, (0, now))
    distance[now]=0
    visited=[False]*(N+1)
    while len(myq)>0:
        first,second=heapq.heappop(myq)
        if distance[second]<first or visited[second]:
            continue
        else:
            visited[second]=True
            for i in range(N+1):
                if far[second][i] != 0 and distance[i]>first+far[second][i]:
                    distance[i] = first+far[second][i]
                    heapq.heappush(myq, (distance[i], i))
    return distance



for tc in range(int(input())):
    N,M,X=map(int, input().split())
    far=[[0]*(N+1) for _ in range(N+1)]
    far2=[[0]*(N+1) for _ in range(N+1)]

    for m in range(M):
        x,y,c=map(int, input().split())
        far[x][y]=c
        far2[y][x]=c

    distance1=dijkstra(X,far)
    distance2=dijkstra(X,far2)

    answer=0
    for i in range(1, N+1):
        tmp=0
        if distance1[i] == 10000000 or distance2[i] == 10000000:
            continue
        answer=max(distance1[i]+distance2[i],answer)
    print('#{} {}'.format(tc+1, answer))