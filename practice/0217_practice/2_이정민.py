def atoi(my_string):
    ans=0
    for c in my_string:
        if '0'<=c<='9':
            ans = ans*10+ord(c)-ord('0')
    return ans

def itoa(my_int):
    ans=''
    while my_int>=10:
        tmp=my_int%10
        ans=chr(ord('0')+tmp)+ans
        my_int= my_int//10
        #print(my_int,ans)
    ans = chr(ord('0') + my_int)+ans
    return ans

input_string=input()
print(atoi(input_string))
print(itoa(atoi(input_string)))
print(type(atoi(input_string)))
print(type(itoa(atoi(input_string))))