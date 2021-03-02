def recursive(idx, sum):
    global answer
    if sum>answer:  # 이미 answer보다 큰 경우
        return
    elif idx==N:    # 배열 전체 순회 완료한경우
        answer=min(sum, answer)     # 더 작은값으로 answer갱신
        return
    else:           # 그 외의 경우
        for i in range(N):
            if not visited[i]:  # 아직 해당 행 사용안했다면
                visited[i]=True
                recursive(idx+1, sum+board[idx][i])
                visited[i]=False

for tc in range(int(input())):
    N=int(input())
    answer=10*50    # 가능한 최대
    board=[]
    visited=[False]*N
    for _ in range(N):
        board.append(list(map(int, input().split())))
    recursive(0,0)

    print('#{} {}'.format(tc+1, answer))