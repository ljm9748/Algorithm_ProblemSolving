def bubble_sort(sort_list):
    for i in range(len(sort_list)-1,0,-1):
        for j in range(i):
            if sort_list[j]>sort_list[j+1]:
                sort_list[j], sort_list[j+1]= sort_list[j+1],sort_list[j]
    return sort_list


# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    len_of_num=int(input())
    tc_numbers=list(map(int, input().split()))

    tc_numbers=bubble_sort(tc_numbers)
    print('#{}'.format(tc + 1), end='')
    for i in range(len_of_num):
        print(' {}'.format(tc_numbers[i]), end='')
    if tc != tc_num - 1:
        print()