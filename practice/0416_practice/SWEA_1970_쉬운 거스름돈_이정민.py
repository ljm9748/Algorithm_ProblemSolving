payback=[50000,10000,5000,1000,500,100,50,10]
for tc in range(int(input())):
    print('#{}'.format(tc+1))
    N= int(input())
    for p in payback:
        print(N//p,end=' ')
        N%=p
    print()