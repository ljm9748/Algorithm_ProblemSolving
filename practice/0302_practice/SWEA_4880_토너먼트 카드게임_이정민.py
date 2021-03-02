def rocksisor(a,b):
    if students[a]==1 and students[b]==3:   # 가위, 보
        return a
    if students[a]==3 and students[b]==1:   # 보, 가위
        return b
    if students[a]>=students[b]:    # 숫자가 같거나 큰 경우
        return a
    else:
        return b

def recursive(start, end):
    # 만약 1명이면
    if end-start==0:
        return end
    # 만약 2명이면
    elif end-start==1:
        return rocksisor(start,end)
    # 이외의 경우
    return rocksisor(recursive(start,(start+end)//2),recursive((start+end)//2+1, end))

for tc in range(int(input())):
    N= int(input())
    students=list(map(int, input().split()))
    print('#{} {}'.format(tc+1, recursive(0,N-1)+1))