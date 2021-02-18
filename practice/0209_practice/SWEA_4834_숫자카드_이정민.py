# 튜플형태로 큰거 반환 (숫자, 장수)
def ismany(a,b):
    return a if a[1]>b[1] else b

# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    len_of_num=int(input())
    cards=list(map(int,list(input())))

    # 카운팅 리스트 생성, 카운트
    count_list=[0]*10
    for card in cards:
        count_list[card] += 1

    # 완성된 리스트로 가장 장수가 많은 카드 선택
    max_count_card=(0, count_list[0])
    for key, card in enumerate(count_list):
        max_count_card= ismany(max_count_card, (key, card))

    print('#{} {} {}'.format(tc+1, max_count_card[0], max_count_card[1]))

