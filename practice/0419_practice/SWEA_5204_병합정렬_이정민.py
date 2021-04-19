def merge_sort(list):
    if len(list)==1:
        return list
    else:
        return merge(merge_sort(list[0:len(list)//2]),merge_sort(list[len(list)//2:len(list)]))

def merge(leftlist, rightlist):
    global answer
    l=r=0
    sortedlist=[]
    if leftlist[-1]>rightlist[-1]:
        answer += 1
    while l<len(leftlist) and r<len(rightlist):
        if leftlist[l]<rightlist[r]:
            sortedlist.append(leftlist[l])
            l += 1
        else:
            sortedlist.append(rightlist[r])
            r += 1
    if l<len(leftlist):
        for i in range(l, len(leftlist)):
            sortedlist.append(leftlist[i])
    elif r<len(rightlist):
        for i in range(r, len(rightlist)):
            sortedlist.append(rightlist[i])
    return sortedlist

for tc in range(int(input())):
    N= int(input())
    answer=0
    inputs=list(map(int, input().split()))
    sorted_list=merge_sort(inputs)
    print('#{} {} {}'.format(tc+1, sorted_list[N//2],answer))
