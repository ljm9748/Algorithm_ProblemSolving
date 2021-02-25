T= int(input())

for tc in range(T):
    students=int(input())
    moves=[]
    for i in range(students):
        moves.append(list(map(int, input().split())))

    time=0  # 필요한 시간
    rooms = [0] * 201   # 복도상황

    for idx in range(len(moves)):
        move=moves[idx]
        move.sort()
        for i in range((move[0]-1)//2, (move[1]-1)//2+1):
            rooms[i]+=1

    time=max(rooms)
    print('#{} {}'.format(tc+1,time))

