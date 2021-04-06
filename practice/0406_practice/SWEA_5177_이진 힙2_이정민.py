import heapq
# 합계찾는 함수
def findsum(node):
    global answer
    if node<1:
        return
    answer += tree[node]
    findsum(node//2)

for tc in range(int(input())):
    N=int(input())
    tree=[]
    inp=list(map(int, input().split()))
    for i in range(N):
        heapq.heappush(tree, inp[i])

    tree=[0]+tree # 1번인덱스부터 시작하기 위해
    answer=0
    findsum(N//2)
    print('#{} {}'.format(tc+1,answer))