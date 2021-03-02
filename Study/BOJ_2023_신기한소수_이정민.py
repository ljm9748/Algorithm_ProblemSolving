import sys
input = sys.stdin.readline
# 처음에는 소수리스트를 만들어 시도하였으나 시간초과나 나서 재시도

N=int(input())

# 소수인지 판별
def isSosu(num):
    if num==0 or num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

# 한자릿수씩 붙여나가며 소수추가
def DFS(num):
    if len(str(num))==N:
        print(num)
    else:
        for i in range(10):
            tmp_num=num*10+i
            if isSosu(tmp_num):
                DFS(tmp_num)

# 한자릿수는 4개밖에 없어 직접입력
DFS(2)
DFS(3)
DFS(5)
DFS(7)