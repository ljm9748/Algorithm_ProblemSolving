def findmax(a,b):
    return a if a>b else b

def findmin(a,b):
    return a if a<b else b

# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    N, M=map(int, input().split())
    tc_numbers=list(map(int, input().split()))

    # 최소 최대구하기 위한 초기화
    tmp_max=-1
    tmp_min=10000*100

    for idx in range(N-M+1):
        tmp_sum=0
        for i in range(idx, idx+M):
            tmp_sum += tc_numbers[i]

        # 최대/최소 구간합 찾기
        tmp_max=findmax(tmp_max, tmp_sum)
        tmp_min=findmin(tmp_min, tmp_sum)

    print('#{} {}'.format(tc+1, tmp_max-tmp_min))
