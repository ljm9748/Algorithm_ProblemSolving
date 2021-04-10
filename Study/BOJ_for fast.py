# A,B=map(int, input().split())
# if A==B:
#     print('==')
# elif A>B:
#     print('>')
# else:
#     print('<')

for tc in range(int(input())):
    n, string=input().split()
    for s in string:
        print(s*int(n), end='')
    print()