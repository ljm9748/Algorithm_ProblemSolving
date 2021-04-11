import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
tree = set()
for _ in range(Q):
    q=int(input())
    last=0
    now=q
    while now>1:
        if now in tree:
            last = now
        now = now//2
    if last==0:
        tree.add(q)
    print(last)
