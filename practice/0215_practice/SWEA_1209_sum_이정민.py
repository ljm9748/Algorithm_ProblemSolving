# tc개수
T=10

for tc in range(10):
    input()
    my_map=[]
    answer=0

    # input으로 표 받으며 가로행의 max구하기
    for i in range(100):
        my_map.append(list(map(int, input().split())))
        tmp_sum=0
        for j in range(100):
            tmp_sum+=my_map[i][j]
        if i==0:
            answer=tmp_sum
        else:
            answer = answer if answer>tmp_sum else tmp_sum

    tmp_topdown = 0
    tmp_downtop = 0
    top_idx=0
    down_idx=99

    # 세로행의 max 구하기
    for i in range(100):
        tmp_sum=0
        for j in range(100):
            tmp_sum += my_map[j][i]
        answer = answer if answer > tmp_sum else tmp_sum

        # 대각선 위->아래
        tmp_topdown += my_map[top_idx][top_idx]
        top_idx+=1

        # 대각선 아래->위
        tmp_downtop += my_map[down_idx][down_idx]
        down_idx -= 1
    answer = answer if answer>tmp_topdown else tmp_topdown
    answer = answer if answer>tmp_downtop else tmp_downtop

    print('#{} {}'.format(tc+1, answer))