def DFS(now):
    if False not in visited:
        return
    else:
        for p in people[now]:
            if not visited[p]:
                visited[p]=True
                DFS(p)

for tc in range(int(input())):
    N,M=map(int, input().split())
    people=[[] for _ in range(N+1)]
    visited=[False]*(N+1)
    visited[0]=True
    answer=0
    for m in range(M):
        f,s=map(int, input().split())
        people[f].append(s)
        people[s].append(f)
    for i in range(1,N+1):
        if not visited[i]:
            answer += 1
            visited[i]=True
            DFS(i)
    print('#{} {}'.format(tc+1, answer))
