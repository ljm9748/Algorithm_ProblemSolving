# 순회하며 더하는 함수
def search(root):
    global answer
    if root<=N:
        search(2*root)
        search(2*root+1)
        answer += tree[root]

for tc in range(int(input())):
    N,M,L= map(int, input().split())
    tree=[0]*(N+1)
    for m in range(M):
        v, value= map(int, input().split())
        tree[v]=value
    answer=0
    search(L)
    print('#{} {}'.format(tc+1, answer))