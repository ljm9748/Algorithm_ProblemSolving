# tc수 입력
T=int(input())

for tc in range(T):
    N=int(input())
    price=list(map(int, input().split()))
    tmp_max=0   # 가장 비싸게 팔 수 있는 가격
    tmp_sum=0   # 지금까지의 이익

    for pr in price[::-1]:  # 뒤에서부터 탐색
        if tmp_max > pr:    # 산가격보다 비싸게 팔수있으면 팔아서 이익남기기
            tmp_sum += tmp_max-pr
        else:
            tmp_max=pr

    print('#{} {}'.format(tc+1, tmp_sum))