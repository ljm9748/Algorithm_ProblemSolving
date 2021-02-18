# 전체 tc 입력
T= int(input())

# tc만큼 반복
for tc in range(T):
    N,K=map(int, input().split()) # N,K입력
    answer=0

    # 비트로 비교
    for i in range(1<<12):
        n_tmp=k_tmp=0
        for j in range(13):
            if i & (1<<j):
                n_tmp+=1
                k_tmp+=j+1
                # 범위넘어가면 break
                if n_tmp>N or k_tmp>K:
                  break

        # 조건에 맞으면 answer에 1 추가
        if n_tmp==N and k_tmp==K:
            answer+=1

    print('#{} {}'.format(tc+1,answer))