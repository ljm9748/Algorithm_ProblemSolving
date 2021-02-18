# 전체 tc
T=int(input())

for tc in range(T):
    D,L,N=map(int, input().split())
    ans=0
    for i in range(N):
        ans+=D+D*i*L*0.01
    print('#{} {}'.format(tc+1, int(ans)))