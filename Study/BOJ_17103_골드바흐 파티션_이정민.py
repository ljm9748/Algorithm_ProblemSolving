def is_sosu(mynum):
    if sosu_list[mynum]:
        return True
    else:
        return False
# 초기 입력
T=int(input())
input_list=[int(input()) for _ in range(T)]
maxnum=max(input_list)

# 소수리스트 만들어놓기
sosu_list=[False]*(maxnum+1)
for i in range(2,maxnum+1):
    tmp_is = True
    for j in range(2, int(i**0.5)+2):
        if i % j ==0:
            tmp_is = False
            break
    sosu_list[i]=tmp_is
sosu_list[2]=True
# print(sosu_list)
# 골드바흐 파티션 개수 찾기
for inp in input_list:
    answer=0
    for i in range(inp//2+1):
        if sosu_list[i] and sosu_list[inp-i]:
            answer += 1
    print(answer)
