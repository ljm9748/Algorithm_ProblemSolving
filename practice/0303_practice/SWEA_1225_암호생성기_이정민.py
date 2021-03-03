T=10
for tc in range(T):
    input()
    minus=1 # 빼야하는 값
    my_queue=list(map(int,input().split())) # 입력값&queue
    run_flag=True

    while run_flag:
        tmp=my_queue.pop(0)
        tmp-=minus
        minus += 1
        if minus==6:    # 한 사이클을 돌았다면
            minus=1
        if tmp<=0:      # 뺀 값이 0보다 작거나 같다면 종료
            tmp=0
            run_flag = False
        my_queue.append(tmp)

    print('#{}'.format(tc+1),end=' ')
    print(*my_queue)
