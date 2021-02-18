# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    N,M= map(int,input().split())
    a_list=list(map(int, input().split()))
    b_list=list(map(int, input().split()))

    if len(a_list)>len(b_list):
        longer_list=a_list
        shorter_list=b_list
    else:
        longer_list=b_list
        shorter_list=a_list

    answer=0 # 초기화 값 설정필요


    for long_idx in range(len(longer_list)-len(shorter_list)+1):
        tmp_answer=0
        for short_idx in range(len(shorter_list)):
            tmp_answer += longer_list[long_idx+short_idx]*shorter_list[short_idx]

        if long_idx==0:
            answer=tmp_answer
        else:
            answer= answer if answer>tmp_answer else tmp_answer

    print('#{} {}'.format(tc+1,answer))


