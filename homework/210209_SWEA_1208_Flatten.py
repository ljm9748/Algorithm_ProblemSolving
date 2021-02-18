
# 전체 tc
tc_num=10
my_count=[0]*101

def findPointMin(point_min):
    for now_point in range(point_min, 101):
        if my_count[now_point]!= 0:
            return now_point
    return 100

def findPointMax(point_max):
    for now_point in range(point_max, 0,-1):
        if my_count[now_point]!= 0:
            return now_point
    return 0

# 그만큼 반복
for tc in range(tc_num):
    dump=int(input())
    numbers=list(map(int, input().split()))

    my_count=[0]*101

    for number in numbers:
        my_count[number] += 1

    point_min=1
    point_max=100
    answer=0

    for i in range(dump):
        if point_max<=point_min:
            break

        point_min=findPointMin(point_min)
        point_max=findPointMax(point_max)

        my_count[point_max] -= 1
        my_count[point_max-1] += 1
        my_count[point_min] -= 1
        my_count[point_min+1] +=1

    point_min = findPointMin(point_min)
    point_max = findPointMax(point_max)

    print('#{} {}'.format(tc+1, point_max-point_min))
