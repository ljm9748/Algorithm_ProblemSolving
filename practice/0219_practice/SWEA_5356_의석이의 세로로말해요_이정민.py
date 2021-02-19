# 전체 tc개수
T=int(input())

# tc만큼 반복
for tc in range(T):
    input_strings=[]    # 의석이의 문자열들
    max_len=0   # 문자열들 중 가장 긴 문자열 길이
    for i in range(5):
        input_strings.append(input())
        max_len= max_len if max_len>len(input_strings[i]) else len(input_strings[i])

    # 프린트하면서 세로로 읽기
    print('#{}'.format(tc+1),end=' ')
    for i in range(max_len):
        for j in range(5):
            if len(input_strings[j])>i: # 문자열의 길이가 다르기때문에 적용
                print(input_strings[j][i],end='')

    # 마지막 tc 엔터 안하기 위해
    if tc != T-1:
        print()