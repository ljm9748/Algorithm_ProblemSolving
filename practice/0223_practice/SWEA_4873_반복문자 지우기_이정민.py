T=int(input())

for tc in range(T):
    input_string=input()
    my_stack=[]
    for char in input_string:   # 입력만큼 순회
        if len(my_stack) == 0:  # stack이 비었다면
            my_stack.append(char)
        elif my_stack[-1] == char:  # stack 마지막과 현재 char가 같다면
            my_stack.pop()
        else:   # 둘다아니라면
            my_stack.append(char)

    print('#{} {}'.format(tc+1, len(my_stack)))