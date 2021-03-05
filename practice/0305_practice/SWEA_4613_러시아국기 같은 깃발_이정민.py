for tc in range(int(input())):
    N,M=map(int,input().split())
    my_map=[list(input()) for _ in range(N)]
    cnt_map=[[0,0,0] for _ in range(N)] # 줄마다 색상 수 있는 리스트[w,b,r]

    # 줄마다 색깔 수 세기
    for idx,my in enumerate(my_map):
        for m in my:
            if m=='W':
                cnt_map[idx][0] += 1
            elif m == 'B':
                cnt_map[idx][1] += 1
            else:
                cnt_map[idx][2] += 1

    answer=M*N
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            tmp_cnt=0
            # 개수 세는 부분[w:0~i줄, b:i+1~j줄, r:(j+1)~(N-1)줄]
            for w in range(0,i+1):
                tmp_cnt += M - cnt_map[w][0]
            for b in range(i+1, j+1):
                tmp_cnt += M - cnt_map[b][1]
            for r in range(j+1, N):
                tmp_cnt += M - cnt_map[r][2]
            answer=min(answer, tmp_cnt)

    print('#{} {}'.format(tc+1, answer))
