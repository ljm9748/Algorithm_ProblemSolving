# tc 수
T=int(input())

# 왼, 오
dx=[-1, -1]
dy=[0, -1]

for tc in range(T):
    N=int(input())
    # 줄만큼 리스트 생성
    triangle=[[] for _ in range(N)]
    triangle[0].append(1)

    for i in range(1,N):    # 두번째줄부터 순회
        for j in range(i+1):    # 추가해야 하는 개수만큼
            # 왼쪽 위, 오른쪽 위의 합 구해서 append
            tmp_sum = 0
            for k in range(2):
                if 0<=j+dy[k]<len(triangle[i-1]):   # 왼쪽위, 오른쪽 위가 있다면
                    tmp_sum += triangle[i+dx[k]][j+dy[k]]
            triangle[i].append(tmp_sum)

    # 정답 출력
    print('#{}'.format(tc+1))
    for i in range(N):
        print(*triangle[i])
