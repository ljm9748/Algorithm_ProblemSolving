def cango(now, chargeridx): # 지금 갈수있는가
    return True if now+K>= chargers[chargeridx] else False

def morego(now, chargeridx): # 한번 더 갈 수 있는가
    if chargeridx>=M:
        return False
    if now+K>= chargers[chargeridx+1]:
        return True
    return False

# 전체 tc 입력
tc_num=int(input())

# 그만큼 반복
for tc in range(tc_num):
    K, N, M=map(int, input().split())
    chargers=list(map(int, input().split()))

    now=0
    now_charger_idx=0
    cnt=0

    while True:
        # 이번연료로 도착
        if now+K>=N:
            break

        # 연료 충전가능
        if cango(now, now_charger_idx):
            if now_charger_idx ==M-1:
                if chargers[now_charger_idx]+K<N:
                    cnt=0
                    break
                cnt +=1
                break
            if morego(now, now_charger_idx):
                now_charger_idx +=1
                continue
            else:
                now = chargers[now_charger_idx]
                cnt += 1
                now_charger_idx +=1

        # 연료 충전불가
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc+1, cnt))



