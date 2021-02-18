# 전체 tc
T= int(input())

for tc in range(T):
    N,M=map(int, input().split())
    my_map=[]
    for _ in range(N):
        my_map.append(list(map(int, input().split())))

    tmp_max=0

    for x in range(N-M+1):
        for y in range(N - M + 1):
            tmp_sum=0
            for j in range(M):
                for k in range(M):
                    tmp_sum += my_map[x+j][y+k]

            tmp_max=tmp_sum if tmp_sum>tmp_max else tmp_max

    print('#{} {}'.format(tc+1, tmp_max))
