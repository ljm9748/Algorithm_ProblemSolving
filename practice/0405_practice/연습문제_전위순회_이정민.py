def prefix(root):
    print(root)
    if tree[root][0] != -1:
        prefix(tree[root][0])
    if tree[root][1] != -1:
        prefix(tree[root][1])

def infix(root):
    if tree[root][0] != -1:
        infix(tree[root][0])
    print(root)
    if tree[root][1] != -1:
        infix(tree[root][1])

def postfix(root):
    if tree[root][0] != -1:
        postfix(tree[root][0])
    if tree[root][1] != -1:
        postfix(tree[root][1])
    print(root)

V=int(input())

tree=[[-1,-1] for _ in range(V+1)]
input_list=list(map(int,input().split()))

for i in range(len(input_list)//2):
    if tree[input_list[2*i]][0]==-1:
        tree[input_list[2*i]][0]=input_list[2*i+1]
    else:
        tree[input_list[2*i]][1]=input_list[2*i+1]
print(tree)
print('--------------prefix--------------')
prefix(1)
print('--------------infix--------------')
infix(1)
print('--------------postfix--------------')
postfix(1)