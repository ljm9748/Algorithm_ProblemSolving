def find_matrix(x,y):   # 행, 열 수 세고 visited표시
    cntx=cnty=0
    for i in range(x,n):
        if my_map[i][y] != 0:
            visited[i][y]=True
            cntx+=1
        else:
            break
    for i in range(y,n):
        if my_map[x][i] !=0:
            visited[x][i] = True
            cnty+=1
        else:
            break
    for i in range(cntx-1):
        for j in range(cnty-1):
            visited[x+i+1][y+j+1]=True

    return cntx,cnty

for tc in range(int(input())):
    n=int(input())
    my_map=[list(map(int, input().split())) for i in range(n)]
    cnt_list=[]
    visited=[[False]*n for _ in range(n)]

    # 행렬 시작하는부분 찾아 행 열 수 세고 리스트에[곱,행,열]넣기
    for x in range(n):
        for y in range(n):
            if my_map[x][y]!=0 and not visited[x][y]:
                cntx,cnty=find_matrix(x,y)
                cnt_list.append([cntx*cnty, cntx, cnty])

    # 조건에 맞게 sort
    answer_list=sorted(cnt_list, key=lambda x:(x[0],x[1]))
    print('#{} {}'.format(tc+1, len(answer_list)),end=' ')
    for answer in answer_list:
        print(*answer[1:],end=' ')
    print()