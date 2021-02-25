T= int(input())
for tc in range(T):
    answer='Possible'
    bread=0
    time=0
    N,M,K=map(int,input().split())
    people=list(map(int, input().split()))
    people.sort()
    for peo in people:
        while peo>=time+M:
            time += M
            bread += K
        if bread>0:
            bread -= 1
        else:
            answer='Impossible'
            break

    print('#{} {}'.format(tc+1, answer))