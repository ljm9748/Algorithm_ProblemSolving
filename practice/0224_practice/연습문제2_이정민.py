arr=[1,2,3,4,5,6,7,8,9,10]
answer=[]

def powerset(idx, mysum):
    if mysum==10:   # 합이 10이 된다면
        print(answer)
        return
    if idx==10: # 모든 idx 순회를 했다면
        return
    else:   # 둘다아니면
        powerset(idx+1, mysum)  # 현재 idx 안 더한 경우
        if arr[idx]+mysum<=10:  # 10 안념어가는 경우만, idx 더한 경우
            answer.append(arr[idx])
            powerset(idx+1, mysum+arr[idx])
            answer.pop()

powerset(0,0)