for tc in range(int(input())):
    N,M=map(int,input().split())
    pizzas=list(map(int,input().split()))
    my_queue=list(range(0,N))   # 화덕 속 들어있는 피자들의 인덱스를 넣기
    next_idx=N                  # 다음에 화덕으로 들어가야 하는 인덱스번호
    while len(my_queue)>1:      # 마지막 하나 남기 전까지
        now_pizza=my_queue.pop(0)   # 지금 꺼낼 수 있는 피자
        pizzas[now_pizza] //=2
        if pizzas[now_pizza] == 0:  # 다 녹았다면
            if next_idx != M:       # 피자가 남았다면
                now_pizza=next_idx
                next_idx+=1
            else:                   # 피자가 안남았다면
                continue
        my_queue.append(now_pizza)

    print('#{} {}'.format(tc+1,my_queue[0]+1))

