import heapq, sys

input=sys.stdin.readline

myq = []
for i in range(int(input())):
    inp=int(input())
    if inp==0:
        if len(myq)==0:
            print(0)
        else:
            print(heapq.heappop(myq))
    else:
        heapq.heappush(myq, inp)