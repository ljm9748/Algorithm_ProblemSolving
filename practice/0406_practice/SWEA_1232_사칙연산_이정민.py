def calc(c, a, b):
    if c == '+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='/':
        return a/b
    else:
        return a*b

def search(root):
    if left[left[root]] == 0:
        a= value[left[root]]
    else:
        a= search(left[root])

    if left[right[root]] == 0:
        b= value[right[root]]
    else:
        b= search(right[root])

    return calc(value[root], a, b)

for tc in range(10):
    N=int(input())
    value=[0]*(N+1)
    left=[0]*(N+1)
    right=[0]*(N+1)

    for n in range(N):
        inp=list(input().split())
        if len(inp)==2:
            value[int(inp[0])]=int(inp[1])
        else:
            value[int(inp[0])]=inp[1]
            left[int(inp[0])]=int(inp[2])
            right[int(inp[0])]=int(inp[3])

    print('#{} {}'.format(tc+1,int(search(1))))