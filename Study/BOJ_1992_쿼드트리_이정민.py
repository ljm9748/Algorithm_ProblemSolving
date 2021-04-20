def DFS(xstart,xend, ystart, yend):
    zero=False
    one=False
    flag=False
    for i in range(xstart,xend+1):
        if flag:
            break
        for j in range(ystart, yend+1):
            if board[i][j]=='1':
                one=True
            else:
                zero=True
            if one and zero:
                flag = True
                break
    if not zero:
        return '1'
    elif not one:
        return '0'
    else:
        result='('
        result += str(DFS(xstart,(xstart+xend)//2, ystart, (ystart+yend)//2))
        result += str(DFS(xstart, (xstart + xend) // 2,(ystart+yend)//2+1,yend))
        result += str(DFS((xstart+xend)//2+1, xend, ystart,(ystart+yend)//2))
        result += str(DFS((xstart + xend) // 2+1, xend,(ystart+yend)//2+1, yend))
        result+=')'
        return result

N=int(input())
board=[list(input()) for _ in range(N)]
result = DFS(0,N-1,0,N-1)
print(result)
