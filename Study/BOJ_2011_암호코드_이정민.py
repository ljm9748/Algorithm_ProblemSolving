def is_alpa_one(str):
    if 1<=int(str)<=9:
        return True
    else:
        return False

def is_alpa_two(str):
    if 10<=int(str)<=26:
        return True
    else:
        return False

input_str=input()
length=len(input_str)
map=[0]*(length+1)
answer=-1
if input_str[0]=='0':
    answer=0
else:
    map[0]=1
    if length>=2:
        if is_alpa_two(input_str[0:2]):
            map[1] += 1
        if is_alpa_one(input_str[1]):
            map[1] += 1

    for i in range(2, length):
        if is_alpa_two(input_str[i - 1:i + 1]):
            map[i] = (map[i] + map[i - 2]) % 1000000
        if is_alpa_one(input_str[i]):
            map[i] = (map[i] + map[i - 1]) % 1000000

    answer=map[length-1]

print(answer)