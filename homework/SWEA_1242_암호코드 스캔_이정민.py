import sys
sys.stdin = open("input.txt", "r")
decode={'112':'0', '122':'1', '221':'2','114':'3', '231':'4','132':'5', '411':'6', '213':'7', '312':'8', '211':'9'}
hexa={'0':'0000', '1':'0001', '2':'0010', '3':'0011','4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011','C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

def secretcheck(num):
    tmp1=0
    for n in range(len(num)):
        tmp1 += int(num[n])
    tmp=tmp1
    tmp += int(num[0]) * 2
    tmp += int(num[2]) * 2
    tmp += int(num[4]) * 2
    tmp += int(num[6]) * 2
    if tmp%10==0:
        return tmp1
    else:
        return 0

for tc in range(int(input())):
    answer=0
    code=set()
    N,M=map(int, input().split())
    for n in range(N):
        tmplist = input()
        # 0으로만 이루어지지 않았다면
        if '1' in tmplist or '2' in tmplist or '3' in tmplist or'4' in tmplist or \
            '5' in tmplist or '6' in tmplist or '7' in tmplist or '8' in tmplist or\
            '9' in tmplist or 'A' in tmplist or 'B' in tmplist or'C' in tmplist or \
            'D' in tmplist or 'E' in tmplist or 'F' in tmplist:
            # 2진수로 전환
            decodelist=''
            for t in range(M):
                decodelist+=hexa[tmplist[t]]
            makecode=''

            # 비율찾기
            x=y=z=0
            for i in range(len(decodelist)-1,-1,-1):
                if decodelist[i] == '1' and y==0 and z==0:
                    x += 1
                elif decodelist[i] == '0' and x!=0 and z==0:
                    y += 1
                elif decodelist[i] == '1' and x!=0 and y!=0:
                    z += 1
                elif decodelist[i] == '0' and x!=0 and y!=0 and z!=0:
                    # 8자리의코드 만드는 과정
                    tmp_min=min(x,y,z)
                    tmpcode=str(x//tmp_min)+str(y//tmp_min)+str(z//tmp_min)
                    makecode=decode[tmpcode]+makecode
                    x=y=z=0
                    # 8자리 완성되었다면
                    if len(makecode)==8:
                        code.add(makecode)
                        makecode=''
    # 집합돌며 정답찾기
    code=list(code)
    for c in range(len(code)):
        answer += secretcheck(code[c])
    print('#{} {}'.format(tc+1, answer))