# string 입력
input_string= input()

answer=''

# 뒤에서부터 읽어서 집어넣기
for char in range(len(input_string)-1,-1,-1):
    answer += input_string[char]

# slice notation이용
slice_notation=input_string[::-1]

# reverse이용
my_reverse=''.join(reversed(input_string))

# swap 이용하기
list_input_string=list(input_string)
for char in range(len(input_string)//2):
    list_input_string[char], list_input_string[(char+1)*-1]=list_input_string[(char+1)*-1], list_input_string[char]

print(answer)
print(slice_notation)
print(my_reverse)
print(''.join(list_input_string))