T= int(input())
for tc in range(T):
    farm=[]
    N=int(input())
    for _ in range(N):
        farm.append(list(map(int, list(input()))))

    answer = sum(farm[N//2])    # 중간줄은 모두 더하기
    # 중간줄 제외 나머지줄 골라서 더하기
    for i in range(N//2):
        answer+= sum(farm[i][N//2-i:N//2+1+i])
        answer+= sum(farm[N-1-i][N//2-i:N//2+1+i])

    print('#{} {}'.format(tc+1, answer))