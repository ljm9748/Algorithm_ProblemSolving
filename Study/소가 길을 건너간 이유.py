import sys
input=sys.stdin.readline

C,N=map(int, input().split())
chicken=[int(input()) for _ in range(C)]
cow=[]
visited=[False]*(C+1)
now_cow=0
now_chi=0
answer=0
for i in range(N):
    cow.append(list(map(int, input().split())))

chicken.sort()
cow.sort(key=lambda x:(x[1]))
# cow.sort(key=lambda x:(x[1],x[0]))

# # 치킨이 안움직여야함(소만커지는경우도 있음)
# while now_chi<C and now_cow<N:
#     if cow[now_cow][0]<=chicken[now_chi]<=cow[now_cow][1]:  # 범위충족
#         answer+= 1
#         now_cow+= 1
#         now_chi+= 1
#     elif cow[now_cow][0]>chicken[now_chi]:  # 치킨이 더 작음
#         now_chi += 1
#     elif cow[now_cow][1]<chicken[now_chi]:  # 치킨이 더 큼
#         now_cow += 1

for co in cow:
    for k in range(C):
        if not visited[k] and co[0]<=chicken[k]<=co[1]:
            visited[k]=True
            answer+=1
            break
        # elif k>c[1]:
        #     break


print(answer)