# tc수
T=int(input())

for tc in range(T):
    sentence, pattern = input().split()


    answer=0

    # 앞에서부터 비교, 길이만큼 비교(범위넘지않게 빼주기)
    idx=0
    while idx<=len(sentence)-len(pattern):
        if sentence[idx:idx+len(pattern)] == pattern:
            answer+=1
            idx+=len(pattern)
        else:
            idx+=1

    print('#{} {}'.format(tc+1, len(sentence)-answer*(len(pattern)-1)))