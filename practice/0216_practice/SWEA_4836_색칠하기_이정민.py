# 전체 tc개수
T=int(input())

# 전체 tc만큼 반복
for tc in range(T):
    # 격자, 정답 초기화
    my_map=[]
    for _ in range(10):
        my_map.append([0]*10)
    answer=0

    N= int(input()) # 칠할 영역의 개수

    # 영역의 개수만큼 반복
    for area in range(N):
        r1,c1,r2,c2,color=map(int, input().split())
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):

                # 안칠해진 경우
                if my_map[r][c]==0:
                    my_map[r][c]=color

                # 보라색이거나 지금 칠하는 색과 같은 색이 칠해져있는 경우
                elif my_map[r][c] == 3 or my_map[r][c]==color:
                    continue

                # 지금 칠한색과 다른 색이 칠해져 있는 경우
                else:
                    answer+=1
                    my_map[r][c]=3

    print('#{} {}'.format(tc+1,answer))
