istring=input()
alpa=['c=','c-','d-','lj','nj','s=','z=']
i=0
answer=0
while i<len(istring):
    answer += 1
    if istring[i:i+3] == 'dz=':
        i += 3
    elif istring[i:i+2] in alpa:
        i += 2
    else:
        i += 1
print(answer)