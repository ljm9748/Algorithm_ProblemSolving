# 순회
def prefix(root):
    global count
    count += 1
    if left[root]:
        prefix(left[root])
    if right[root]:
        prefix(right[root])

for tc in range(int(input())):
    E,N=map(int, input().split())
    left=[0]*(E+2)
    right=[0]*(E+2)
    inp=list(map(int, input().split()))
    count=0

    for i in range(0, len(inp), 2):
        if not left[inp[i]]:
            left[inp[i]]=inp[i+1]
        else:
            right[inp[i]]=inp[i+1]
    
    # 탐색시작
    prefix(N)
    print('#{} {}'.format(tc+1, count))