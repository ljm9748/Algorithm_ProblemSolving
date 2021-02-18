# 전체 tc
T=int(input())

# 그만큼 반복
for tc in range(T):
    str1=input()
    str2=input()

    my_dict={}
    # str1으로 dictionary만들기
    for c in str1:
        if my_dict.get(c) is None:
            my_dict[c]=0

    # dic에 있으면 str2에 있을때마다 1더하기
    for c in str2:
        if my_dict.get(c) is not None:
            my_dict[c]+=1

    # dictionary에서 max값 찾기
    max_val=my_dict[str1[0]]
    for key in my_dict:
        #print(key)
        if my_dict[key]>max_val:
            max_val=my_dict[key]

    print('#{} {}'.format(tc+1, max_val))