length=int(input())
lines=list(map(int,input().split()))
lines.sort()
answer=0
for line in lines:
    answer+=length*line
    length-=1

print(answer)