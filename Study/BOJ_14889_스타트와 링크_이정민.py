N=int(input())
my_map=[list(map(int, input().split())) for n in range(N)]

def find_team(person,count):
    if count==N//2:
        calc()
    else:
        if person<N:
            find_team(person+1,count)
            start_team.append(person)
            find_team(person+1, count+1)
            start_team.pop()

def calc():
    global abs_min
    start_sum=0
    link_sum=0
    link_team=list(range(N))
    for i in start_team:
        link_team.remove(i)
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            start_sum+=my_map[start_team[i]][start_team[j]]
            start_sum+=my_map[start_team[j]][start_team[i]]
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            link_sum+=my_map[link_team[i]][link_team[j]]
            link_sum+=my_map[link_team[j]][link_team[i]]

    abs_min= min(abs_min,abs(link_sum-start_sum))

start_team=[]
abs_min=100*10
find_team(1,0)
start_team.append(0)
find_team(1,1)
start_team.pop(0)
print(abs_min)