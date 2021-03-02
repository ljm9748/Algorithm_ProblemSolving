# 계산하는 함수
def calc(a,b,cal):
    if cal=='+':
        return a+b
    if cal=='*':
        return a*b
    if cal=='-':
        return a-b
    if cal=='/':
        return a//b

for tc in range(int(input())):
    answer="error"
    input_list=list(input().split())
    stack=[]    # 숫자들을 보관해놓을 곳
    # 식 순회
    for i in input_list:
        if i.isdigit(): # 숫자이면
            stack.append(int(i))
        elif i=='.':    # 마치는 문자일때
            if len(stack)>1:    # stack에 수가 남아있으면 계산 다 안된것
                break
            answer=stack[0]     # 계산 마쳤으면 answer갱신
            break
        else:           # 연산자이면
            if len(stack)<2:    # 만약 계산가능한 숫자가 부족하면
                break
            b=stack.pop()
            a=stack.pop()
            stack.append(calc(a,b,i))
    print('#{} {}'.format(tc+1, answer))