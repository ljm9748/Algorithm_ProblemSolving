import sys

sys.stdin = open("input.txt", "r")
for num in range(10):
    T = int(input())
    print(T)
    print
    mylist=list(map(int,input().split()))
    print(mylist)

    answer=0

    # 건물없는 땅이아닌 2번 인덱스부터 뒤에 두개 제외하고 다 돌며 찾기
    for i in range(2,T-2):
        tmp_max = -1

        # 앞땅 2개와 비교
        if mylist[i]>mylist[i-1] and mylist[i]>mylist[i-2]:
            tmp_max= mylist[i-1] if mylist[i-1]>mylist[i-2] else mylist[i-2]
        else:
            continue

        # 뒤 땅 2개와 비교
        if mylist[i]>mylist[i+1] and mylist[i]> mylist[i+2]:
            tmp_max= mylist[i+1] if mylist[i+1]>tmp_max else tmp_max
            tmp_max = tmp_max if tmp_max > mylist[i + 2] else mylist[i + 2]
        else:
            continue

        answer += mylist[i]-tmp_max

    print("#{} {}".format(num+1, answer))



