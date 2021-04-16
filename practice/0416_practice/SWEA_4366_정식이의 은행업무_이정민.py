def bintonum():
    two=1
    tmpsum=0
    for i in range(len(bininput)-1,-1,-1):
        tmpsum+=bininput[i]*two
        two*=2
    return tmpsum

def tritonum():
    tri = 1
    tmpsum = 0
    for i in range(len(triinput)-1, -1, -1):
        tmpsum += triinput[i] * tri
        tri *= 3
    return tmpsum

for tc in range(int(input())):
    bin=[]
    bininput=list(map(int, list(input())))
    triinput=list(map(int,list(input())))
    for i in range(len(bininput)):
        if bininput[i]==0:
            bininput[i]=1
            bin.append(bintonum())
            bininput[i]=0
        else:
            bininput[i]=0
            bin.append(bintonum())
            bininput[i]=1
    flag=False
    for i in range(len(triinput)):
        if flag:
            break
        for j in range(2):
            triinput[i]=(triinput[i]+1)%3
            tmpanswer=tritonum()
            if tmpanswer in bin:
                print('#{} {}'.format(tc+1,tmpanswer))
                flag=True
                break
        triinput[i] = (triinput[i] + 1) % 3



