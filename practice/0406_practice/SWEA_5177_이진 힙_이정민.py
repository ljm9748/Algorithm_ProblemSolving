# 트리 자리바꿔주는 함수
def treecheck(last):
    if last<0:
        return
    if tree[last]<tree[last//2]:
        tree[last],tree[last//2]=tree[last//2],tree[last]
        treecheck(last//2)

# 합계찾는 함수
def findsum(node):
    global answer
    if node<1:
        return
    answer += tree[node]
    findsum(node//2)


for tc in range(int(input())):
    N=int(input())
    tree = [0]*(N+1)
    inp=list(map(int, input().split()))
    for i in range(N):
        tree[i+1]=inp[i]
        treecheck(i+1)
    answer=0
    findsum(N//2)
    print('#{} {}'.format(tc+1,answer))