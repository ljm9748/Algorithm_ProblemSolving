# 중위순회하면서 자식수 세기
def infix(root):
    global answer
    if left[root]!=0:
        infix(left[root])
    answer += 1
    if right[root]!=0:
        infix(right[root])

# 입력받기
for tc in range(int(input())):
    V,N=map(int, input().split())
    left=[0]*(V+1)
    right=[0]*(V+1)
    inplist=list(map(int, input().split()))

    # 입력받은 내용을 기반으로 트리 만들기
    for i in range(0,len(inplist),2):
        if left[inplist[i]] ==0:
            left[inplist[i]] = inplist[i+1]
        else:
            right[inplist[i]] = inplist[i+1]

    answer=-1     # 본인은 포함하지 않기 때문에 -1에서 시작
    infix(N)      # 순회 시작

    print('#{} {}'.format(tc+1, answer))