def find_moo(now, nth, tmp_len):
    global answer
    # print(now, nth, tmp_len)
    if nth==0:
        answer=moo[now-1]
        return
    else:
        bef=(tmp_len - (3+nth))//2
        if now<=bef:
            find_moo(now, nth-1, bef)
        elif bef < now <= bef + nth+3:
            if now == bef+1:
                answer='m'
                return
            else:
                answer='o'
                return
        else:
            find_moo(now-(bef+(3+nth)), nth-1, bef)
N=int(input())

tmp_len=3
nth=0
moo='moo'
anser=''
if tmp_len<3:
    nth=0
    tmp_len=3
else:
    while tmp_len*2+3+nth<N:
        nth += 1
        tmp_len = tmp_len*2+3+nth

    nth +=1
    tmp_len = tmp_len*2+3+nth
# print(nth, tmp_len)
find_moo(N, nth, tmp_len)


print(answer)