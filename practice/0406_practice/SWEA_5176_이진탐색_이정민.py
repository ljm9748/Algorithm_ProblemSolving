# 배열에 트리만들기
def make(idx):
    global number
    if idx<=N:
        make(2*idx)     # 왼쪽 서브트리
        tree[idx]=number
        number+=1
        make(2*idx+1)   # 오른쪽 서브트리


for tc in range(int(input())):
    N=int(input())
    tree=[0]*(N+1)
    number=1
    make(1)

    print('#{} {} {}'.format(tc+1, tree[1], tree[N//2]))