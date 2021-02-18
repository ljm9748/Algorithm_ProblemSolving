T = 10
for tc in range(T):
    tmp = input()
    garo_list = []
    longest = 1
    # print(tmp[0:3])
    # print(tmp[3:0:-1])
    # for word_len in range(1,10):
    #     for k in range(10 - word_len + 1):
    #         print(word_len, k, tmp[k:k+word_len//2],tmp[k+word_len-1: k+word_len-1-(word_len//2):-1])

    # 가로행 처리
    for i in range(100):
        garo_list.append(input())
        for word_len in range(100):
            for k in range(100 - word_len + 1):
                if garo_list[i][k:k + word_len // 2] == garo_list[i][
                                                        k + word_len - 1:k + word_len - 1 - (word_len // 2):-1]:
                    longest = longest if longest > word_len else word_len

    sero_list = [''] * 100
    # 세로행 가로화
    for garo in garo_list:
        for i in range(100):
            sero_list[i] += garo[i]

    # 세로행 처리
    for i in range(100):
        for word_len in range(100):
            for k in range(100 - word_len + 1):
                if sero_list[i][k:k + word_len // 2] == sero_list[i][
                                                        k + word_len - 1:k + word_len - 1 - (word_len // 2):-1]:
                    longest = longest if longest > word_len else word_len

    print('#{} {}'.format(tc+1,longest))