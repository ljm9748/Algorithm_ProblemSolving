import sys
input = sys.stdin.readline

def color_same():       # 같은색인지 판별
    for card in cards:
        if len(cards.get(card)) == 5:
            return True
        elif len(cards.get(card)) == 0:
            continue
        else:
            return False

def num_growup():       # 숫자가 연속인지 판별
    tmp_list=[]
    count=[0]*10
    for card in cards:
        tmp_list+=cards.get(card)
        for c in cards.get(card):
            if count[c] ==1:
                return False,0
            else:
                count[c] += 1
    tmp_list.sort()
    if tmp_list[-1]-tmp_list[0]==4:
        return True, tmp_list[-1]
    else:
        return False, 0

def same_num(howmany,fromfront):         # 원하는 개수를 가진 인덱스번호 찾기 없으면 0
    count=[0]*10
    for card in cards:
        for c in cards.get(card):
            count[c] += 1
    if fromfront:
        for i in range(1,10):
            if count[i] == howmany:
                return i
    else:
        for i in range(9,0,-1):
            if count[i] == howmany:
                return i
    return 0


def find_score():
    # 규칙1
    if color_same():
        is_grow, max_num=num_growup()
        if is_grow:
            print(max_num+900)
            return

    # 규칙2
    num_idx= same_num(4,True)
    if num_idx != 0:
        print(num_idx+800)
        return

    # 규칙3
    num_idx=same_num(3,True)
    if num_idx != 0:
        answer = num_idx*10
        num_idx2=same_num(2,True)
        if num_idx2 != 0:
            answer += num_idx2+700
            print(answer)
            return
        elif not color_same():  # 규칙 6
            print(num_idx+400)
            return

    # 규칙4
    if color_same():
        tmp_list=[]
        for card in cards:
            tmp_list += cards.get(card)
        tmp_list.sort()
        print(tmp_list[-1]+600)
        return

    # 규칙5
    is_true, max_num=num_growup()
    if is_true:
        print(500+max_num)
        return

    # 규칙7
    num_idx=same_num(2,True)
    if num_idx !=0:
        answer = num_idx
        num_idx2=same_num(2,False)
        if num_idx2 != num_idx:
            answer += num_idx2*10 + 300
            print(answer)
            return
        else:           # 규칙8
            print(answer+200)
            return

    # 규칙9
    tmp_list = []
    for card in cards:
        tmp_list += cards.get(card)
    tmp_list.sort()
    print(tmp_list[-1]+100)
    return

# 입력부분
cards={}

for i in range(5):
    color, number = input().split()
    if cards.get(color) is None:
        cards[color] = [int(number)]
    else:
        cards[color].append(int(number))

find_score()