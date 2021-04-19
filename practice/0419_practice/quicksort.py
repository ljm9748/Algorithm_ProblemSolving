inputlist=list(map(int, input().split()))
def partition(arr, start, end):
    p=start
    left=start+1
    right=end
    while True:
        if right<left:
            break
        if arr[left]<=arr[start]:
            left += 1
        elif arr[right]>=arr[start]:
            right -= 1
        else:
            arr[left],arr[right]=arr[right],arr[left]
    arr[start],arr[right]=arr[right],arr[start]
    return right

def quick_sort(arr, start, end):
    if start<end:
        p=partition(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)
    return arr

print(quick_sort(inputlist,0,len(inputlist)-1))