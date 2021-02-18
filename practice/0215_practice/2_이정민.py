arr=list(map(int,input().split()))
answer=False
for i in range(1,1<<len(arr)):
    tmp_sum = 0
    flag=False
    for j in range(len(arr)+1):
        if i & (1<<j):
            flag=True
            tmp_sum+=arr[j]
            #print(arr[j], end=' ')
    #print()
    if (flag==True and tmp_sum==0):
        answer=True
        break
print('부분집합의 합이 0이되는것이 존재하는가? {}'.format(answer))