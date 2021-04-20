def isokay(n, new):
    now=n
    if now == new:
        return False
    else:
        return True
for tc in range(int(input())):
    N,M=map(int, input().split())
    nlist=list(map(int, input().split()))
    nlist.sort()
    mlist=list(map(int, input().split()))
    answer=0
    for m in mlist:
        now=0
        l=0
        r=N-1
        while True:
            mid=(l+r)//2

            if nlist[mid] == m:
                answer += 1
                break
            elif nlist[mid]>m:
                r=mid-1
                if now==0:
                    now=-1
                else:
                    if isokay(now,-1):
                        now=-1
                    else:
                        break
            elif nlist[mid]<m:
                l=mid+1
                if now==0:
                    now=1
                else:
                    if isokay(now,1):
                        now=1
                    else:
                        break
            else:
                break
    print('#{} {}'.format(tc+1, answer))
