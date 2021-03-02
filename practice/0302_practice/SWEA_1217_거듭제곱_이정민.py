def recursive(n, num):
    if num==1:
        return n
    else:
        return recursive(n, num//2)*recursive(n, num-num//2)

for tc in range(10):
    input()
    N,M=map(int,input().split())
    answer=recursive(N,M)
    print('#{} {}'.format(tc+1, answer))