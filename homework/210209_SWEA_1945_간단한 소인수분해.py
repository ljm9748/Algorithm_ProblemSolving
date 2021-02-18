# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    input_num=int(input())

    answer_list=[0]*5
    sosus=[2,3,5,7,11]
    for sosu in range(len(sosus)):
        while input_num%sosus[sosu] == 0:
            input_num = input_num // sosus[sosu]
            answer_list[sosu] += 1

    print('#{} {} {} {} {} {}'.format(tc+1, answer_list[0], answer_list[1], answer_list[2], answer_list[3], answer_list[4]))
