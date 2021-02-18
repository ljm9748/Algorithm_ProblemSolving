# 전체 tc
T=int(input())
input_list=[]

def swap(a,b):
    global input_list
    if input_list[a]>input_list[b]:
        input_list[a],input_list[b]=input_list[b],input_list[a]

# 오름차순 정렬
for tc in range(T):
    N= int(input())
    input_list=list(map(int, input().split()))
    for i in range(N,0,-1):
        for j in range(i-1):
            swap(j, j+1)

    # 출력
    cnt=0
    print('#{} '.format(tc+1),end='')
    for i in range(N//2):
        print(input_list[N-1-i], end=' ')
        print(input_list[i], end=' ')
        cnt+=2
        if(cnt>=10):
            break

    # 홀수개이고 10개 안찼을 경우
    if N%2==1 and cnt<10:
        print(input_list[N//2], end=' ')

    # 마지막 제외 엔터추가
    if tc!=T-1:
        print()