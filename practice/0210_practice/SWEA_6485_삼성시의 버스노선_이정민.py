# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    N= int(input())
    bus_list=[]
    for _ in range(N):
        A,B= map(int,input().split())
        bus_list.append((A,B))
    P=int(input())
    busstop_list=[]
    answer_list=[0]*P
    for _ in range(P):
        busstop_list.append(int(input()))

    for bus in bus_list:
        for busstop_idx in range(P):
            if busstop_list[busstop_idx] >= bus[0] and busstop_list[busstop_idx]<=bus[1]:
                answer_list[busstop_idx] += 1
    print('#{}'.format(tc+1), end='')
    for i in range(P):
        print(' {}'.format(answer_list[i]), end='')
    if tc != tc_num-1:
        print()


