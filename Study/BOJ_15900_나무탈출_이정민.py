# N =int(input())
# tree=[[0,True] for _ in range(N+1)]

# for i in range(N-1):
#     a, b= map(int,input().split())
#     if tree[a][0] != 0 or a==1:
#         tree[b][0] = tree[a][0]+1
#         tree[a][1] = False
#     else:
#         tree[a][0] = tree[b][0] + 1
#         tree[b][1] = False
# print(tree)
# tmp_sum=0
# for i in range(1,N+1):
#     if tree[i][1]:
#         tmp_sum += tree[i][0]
#
# if tmp_sum%2==0:
#     print('No')
# else:
#     print('Yes')

from collections import deque
N =int(input())

# 연결이 나중에 되는 경우가 있다면?
tree=[[] for i in range(N+1)]
visited=[False]*(N+1)
q=deque()
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
q.append([1,0])
visited[1]=True
tmp_sum=0
while len(q)>0:
    front=q.popleft()

    is_leaf=True
    for t in tree[front[0]]:
        if not visited[t]:
            is_leaf=False
            visited[t]=True
            q.append([t, front[1]+1])
    if is_leaf:
        tmp_sum+=front[1]

if tmp_sum%2==0:
    print('No')
else:
    print('Yes')