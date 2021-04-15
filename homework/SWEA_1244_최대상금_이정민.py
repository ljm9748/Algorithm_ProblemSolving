import copy
def playswap(time):
    global answer
    if [inp_list,time] in visited:
        return
    else:
        tmp=copy.deepcopy(inp_list)
        visited.append([tmp, time])


    if time == swap:
        tmpstring=''.join(inp_list)
        answer=max(answer, int(tmpstring))
        return
    else:
        for i in range(len(inp_list)-1):
            for j in range(i+1,len(inp_list)):
                print(i,j, inp_list)
                inp_list[i], inp_list[j]= inp_list[j], inp_list[i]
                playswap(time+1)
                inp_list[j], inp_list[i] = inp_list[i], inp_list[j]

for tc in range(int(input())):
    answer=0
    tmpinp, swap=input().split()
    swap=int(swap)
    visited=[]
    inp_list=list(tmpinp)
    playswap(0)
    print('#{} {}'.format(tc+1, answer))