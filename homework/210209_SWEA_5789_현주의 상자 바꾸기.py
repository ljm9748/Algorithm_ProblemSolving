# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    N, Q=map(int, input().split())
    my_list= [0]*N

    for i in range(1,Q+1):
        L,R=map(int, input().split())
        for j in range(L-1, R):
            my_list[j]=i
    print('#{}'.format(tc+1), end=' ')
    for i in my_list:
        print(i, end=' ')
    if tc != tc_num+1:
        print()

