for tc in range(int(input())):
    N,M= map(int, input().split())
    inputq=list(map(int, input().split()))
    # M번만큼 순회
    for m in range(M):
        tmp=inputq.pop(0)
        inputq.append(tmp)
    print('#{} {}'.format(tc+1, inputq[0]))