for tc in range(int(input())):
    # 입력받고 트럭과 컨테이너들 큰 순서로 정렬
    N,M= map(int, input().split())
    containers=list(map(int, input().split()))
    containers.sort(reverse=True)
    truck=list(map(int, input().split()))
    truck.sort(reverse=True)
    answer=0
    c = 0
    # 트럭만큼 돌리면서 가장큰 컨테이너 가져가기
    for t in truck:
        while c<len(containers):
           if containers[c]<=t:
               answer+=containers[c]
               c+=1
               break
           else:
               c+=1

    print('#{} {}'.format(tc+1, answer))