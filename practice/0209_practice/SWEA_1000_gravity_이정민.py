def findmax(a,b):
    return a if a>b else b

num_of_input=int(input())
for nth_try in range(num_of_input):
    list_len=int(input())
    first_list=list(map(int ,input().split()))
    answer=0

    for key,boxs in enumerate(first_list):
        if boxs!=0:
            tmp = key+1
            for i in range(key+1, list_len):
                if boxs<=first_list[i]:
                    tmp +=1
            answer=findmax(answer,list_len-tmp)


    print("#{} {}".format(nth_try+1,answer))


