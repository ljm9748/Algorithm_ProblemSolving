def DFS(num):
    if num<2:
        return str(num)
    else:
        return str(DFS(num//2))+str(num%2)

for tc in range(int(input())):
    N,M= map(int, input().split())
    tmp_bit=DFS(M)
    if tmp_bit[-1*N:]=='1'*N:
        print('#{} ON'.format(tc+1))
    else:
        print('#{} OFF'.format(tc + 1))
