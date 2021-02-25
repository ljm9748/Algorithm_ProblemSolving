T=int(input())

for tc in range(T):
    sudoku = []
    finish=False
    answer=1
    check_list=[0]*10
    # sudoku 입력
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    # 가로줄 체크
    for i in range(9):
        if finish:
            break
        check_list=[0]*10
        for j in sudoku[i]:
            if check_list[j] == 1:
                answer=0
                finish=True
                break
            else:
                check_list[j]=1

    # 세로줄 체크
    for i in range(9):
        if finish:
            break
        check_list=[0]*10
        for j in range(9):
            if check_list[sudoku[j][i]]==1:
                answer = 0
                finish = True
                break
            else:
                check_list[sudoku[j][i]]=1

    # 사각형 체크
    for i in range(3):
        if finish:
            break
        for j in range(3):
            check_list=[0]*10
            for x in range(3):
                for y in range(3):
                    if check_list[sudoku[i*3+x][j*3+y]] == 1:
                        answer = 0
                        finish = True
                        break
                    else:
                        check_list[sudoku[i * 3 + x][j * 3 + y]] = 1
    print('#{} {}'.format(tc+1, answer))