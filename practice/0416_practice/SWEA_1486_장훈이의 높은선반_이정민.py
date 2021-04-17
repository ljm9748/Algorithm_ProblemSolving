def DFS(nowsum, trash, idx):
    global answer
    if idx==N+1:
        return
    if sumpeople-trash<B:   # 가망없는경우
        return
    elif B<=nowsum:
        answer=min(nowsum-B,answer)
        return
    else:
        DFS(people[idx]+nowsum, trash, idx+1)
        DFS(nowsum, trash+people[idx], idx+1)


for tc in range(int(input())):
    N,B=map(int, input().split())
    people=list(map(int, input().split()))
    sumpeople= answer = sum(people)
    DFS(people[0],0,1)
    DFS(0,people[0],1)
    print('#{} {}'.format(tc+1, answer))