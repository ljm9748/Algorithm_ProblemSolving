
priorities=[['*',2,2], ['/',2,2], ['+',1,1],['-',1,1],['(',0,3]]  # 토큰, isp, icp

# 중위 -> 후위 함수
def infixToPost(infix):
    postfix = ''
    my_stack = []
    for i in infix:
        if i.isdigit():
            postfix += i
        elif i ==')':
            while my_stack[-1][0] != '(':
                postfix += my_stack[-1][0]
                my_stack.pop()
            my_stack.pop()
        else:
            for priority in priorities:
                if i == priority[0]:
                    while len(my_stack)>0 and my_stack[-1][1]>=priority[2]:
                        postfix += my_stack[-1][0]
                        my_stack.pop()
                    my_stack.append(priority)
                    break
    while len(my_stack)>0:
        postfix += my_stack[-1][0]
        my_stack.pop()
    return postfix

# 계산해주는 함수
def calc(cal, A, B):
    if cal=='+':
        return A+B
    if cal=='-':
        return A-+B
    if cal=='/':
        return A/B
    if cal=='*':
        return A*B
for tc in range(10):
    input()
    infix = input()
    # 값을 계산하는 부분
    calc_stack=[]
    postfix=infixToPost(infix)
    for post in postfix:
        if post.isdigit():
            calc_stack.append(int(post))
        else:
            B=calc_stack.pop()
            A=calc_stack.pop()
            calc_stack.append(calc(post, A, B))

    print('#{} {}'.format(tc+1,calc_stack[0]))