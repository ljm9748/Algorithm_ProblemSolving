# 전체 tc
T=int(input())

for tc in range(T):
    N=int(input())
    input_list=list(map(int, input().split()))

    for i in range(N):
        min_idx=i
        for j in range(i,N):
            if input_list[min_idx]>input_list[j]:
                min_idx=j
        input_list[i],input_list[min_idx]=input_list[min_idx],input_list[i]

    print('#{} '.format(tc+1), end='')
    print(*input_list)
