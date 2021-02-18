# 전체 tc입력
T= int(input())

# tc만큼 반복
for tc in range(T):
    str1=input()
    str2=input()
    answer=0

    # 앞에서부터 비교, 길이만큼 비교(범위넘지않게 빼주기)
    for char2_idx in range(len(str2)-len(str1)+1):
        if str2[char2_idx:char2_idx+len(str1)] == str1:
            answer=1
            break


    print('#{} {}'.format(tc+1, answer))



