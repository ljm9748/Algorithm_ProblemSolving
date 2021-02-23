# tc개수
T = int(input())

paper=[0,1,3,]
for tc in range(T):
    N= int(input())//10
    if len(paper)-1<N:
        for i in range(len(paper), N+1):
            paper.append(paper[i-2]*2+paper[i-1])
    print(paper)

    print('#{} {}'.format(tc+1, paper[N]))