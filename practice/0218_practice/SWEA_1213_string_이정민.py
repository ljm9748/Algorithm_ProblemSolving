T=10
for tc in range(T):
    input()
    pattern=input()
    sentence=input()

    answer=0

    # 앞에서부터 비교, 길이만큼 비교(범위넘지않게 빼주기)
    for idx in range(len(sentence)-len(pattern)+1):
        if sentence[idx:idx+len(pattern)] == pattern:
            answer+=1

    print('#{} {}'.format(tc+1, answer))