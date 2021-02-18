# 전체 tc입력
T= int(input())

# tc만큼 반복
for tc in range(T):
    N,M=map(int,input().split())
    my_map=[]
    for _ in range(N):
        my_map.append(list(input()))
    answer=''

    find_answer=False   # 정답이 나왔는지 체크해주는 flag

    # 가로방향 탐색
    for i in range(N):
        if find_answer:
            break
        for j in range(N-M+1):
            if find_answer:
                break
            # 반만큼 비교
            for k in range(M//2):
                if my_map[i][j+k] == my_map[i][j+M-1-k]:
                    # 반 전체 비교했다면 (회문이라면)
                    if k==M//2-1:
                        answer += ''.join(my_map[i][j:j+M])
                        find_answer=True
                        break
                else:
                    break

    # 세로방향 탐색
    for i in range(N - M + 1):
        if find_answer:
            break
        for j in range(N):
            if find_answer:
                break
            # 반만큼 비교
            for k in range(M // 2): # 반 전체 비교했다면 (회문이라면)
                if my_map[i+k][j]== my_map[i+M-1-k][j]:
                    if k==M//2-1:
                        for x in range(M):
                            answer += my_map[i+x][j]
                            find_answer=True
                        break
                else:
                    break
    print('#{} {}'.format(tc + 1, answer))





