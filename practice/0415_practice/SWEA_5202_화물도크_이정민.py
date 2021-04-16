for tc in range(int(input())):
    N= int(input())
    truck=[list(map(int, input().split())) for _ in range(N)]
    truck.sort(key=lambda x:x[1])   # 끝나는시간 작은순 정력
    answer=1
    now=0   # 지금 화물차
    new=1   # 다음 화물차 후보
    while now<N and new<N:
        if truck[new][0]>=truck[now][1]:
            answer+=1
            now=new
            new+=1
        else:
            new+=1
    print('#{} {}'.format(tc+1, answer))