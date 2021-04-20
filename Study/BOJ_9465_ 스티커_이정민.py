for tc in range(int(input())):
    N=int(input())
    inputlist=[list(map(int, input().split())) for _ in range(2)]
    mymap=[[0]*N for _ in range(3)]
    mymap[0][0]=inputlist[0][0]
    mymap[1][0]=inputlist[1][0]
    for i in range(1, N):
        mymap[0][i]=max(mymap[1][i-1], mymap[2][i-1])+inputlist[0][i]
        mymap[1][i]=max(mymap[0][i-1], mymap[2][i-1])+inputlist[1][i]
        mymap[2][i]=max(mymap[0][i-1],mymap[1][i-1], mymap[2][i-1])
    print(max(mymap[0][N-1], mymap[1][N-1], mymap[2][N-1]))