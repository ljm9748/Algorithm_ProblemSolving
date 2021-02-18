def findmax(a,b):
    return a if a>b else b

def findmin(a,b):
    return a if a<b else b

# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    len_of_num=int(input())
    tc_numbers=list(map(int, input().split()))

    # 초기화
    my_min=my_max=tc_numbers[0]
    for tc_number in tc_numbers:
        my_min=findmin(my_min,tc_number)
        my_max = findmax(my_max, tc_number)

    # 출력
    print('#{} {}'.format(tc+1, my_max-my_min))
