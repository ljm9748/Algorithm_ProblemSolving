class Stack():
    def __init__(self):
        self.stack=[]

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def push(self, new):
        self.stack.append(new)

    def pop(self):
        if len(self.stack) !=0 :
            return self.stack.pop()

    def peek(self):
        print(self.stack[-1])

T=10
# 괄호 오른쪽왼쪽 모음
dleft=['(','[','{','<']
dright=[')',']','}','>']

for tc in range(T):
    input_len=int(input())
    input_list=list(input())
    my_stack=Stack()
    answer=1
    finish_flag=False


    for i in range(input_len):  # 입력괄호길이만큼 순회
        if finish_flag:
            break
        for j in range(4):  # 이미 지정해준 괄호들 리스트만큼 순회
            if input_list[i] == dleft[j]:   # 왼쪽 괄호라면
                my_stack.push(input_list[i])
                break
            elif input_list[i] == dright[j]:    # 오른쪽괄호라면
                if my_stack.__len__() ==0:
                    answer=0
                    finish_flag = True
                elif my_stack.pop() != dleft[j]:
                    answer=0
                    finish_flag = True
                else:
                    break

    # 스택에 남은게 있다면
    if my_stack.__len__() !=0:
        answer=0
    print('#{} {}'.format(tc+1, answer))