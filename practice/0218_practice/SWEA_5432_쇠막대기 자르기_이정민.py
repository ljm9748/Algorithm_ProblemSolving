# TC 개수 입력
T= int(input())

for tc in range(T):
    input_string=input()

    now_poll=0  # 지금 세고있는 구간 막대기 수
    answer=0    # 조각 총개수

    for i in range(len(input_string)):
        if i<len(input_string)-1 and input_string[i:i+2]=='()':
            answer += now_poll
            now_poll+=1 # 뒤에 한번 더 빼지기 때문
        elif input_string[i]=='(':
            answer += 1
            now_poll += 1
        elif input_string[i]==')':
            now_poll -=1

    print('#{} {}'.format(tc+1, answer))