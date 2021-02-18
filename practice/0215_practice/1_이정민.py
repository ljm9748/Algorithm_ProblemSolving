from random import *

my_map=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
answer=[]

for _ in range(5):
    tmp_list=[]
    answer.append([0]*5)
    for _ in range(5):
        tmp_list.append(randint(1, 100))
    my_map.append(tmp_list)

for i in range(5):
    for j in range(5):
        for k in range(4):
            if 0<=i+dx[k]<=4 and 0<=j+dy[k]<=4:
                answer[i][j]+= abs(my_map[i][j]-my_map[i+dx[k]][j+dy[k]])

print(answer)
