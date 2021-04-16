def wincheck(cards):
    for i in range(10):
        if cards[i]>=3:
            return True
    for i in range(8):
        if cards[i]>0 and cards[i+1]>0 and cards[i+2]>0:
            return True
    return False

for tc in range(int(input())):
    inplist=list(map(int, input().split()))
    p1=[0]*10
    p2=[0]*10
    answer=0
    for i in range(12):
        if i%2==0:
            p1[inplist[i]] += 1
            if i>=6:
                if wincheck(p1):
                    answer=1
                    break
        else:
            p2[inplist[i]] += 1
            if i>=6:
                if wincheck(p2):
                    answer=2
                    break
    print('#{} {}'.format(tc+1, answer))