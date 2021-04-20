def DFS(cnt, power, idx):
    global answer
    if idx==N:
        answer=min(answer,cnt)
        return
    if cnt>=answer:
        return
    else:
        if power>=1:
            DFS(cnt, power -1, idx+1)
        if power-1<busstops[idx]:
            DFS(cnt+1, busstops[idx]-1, idx+1)

for tc in range(int(input())):
    busstops=list(map(int, input().split()))
    N=busstops[0]
    answer=N
    DFS(0,busstops[1],1)
    print('#{} {}'.format(tc+1, answer))