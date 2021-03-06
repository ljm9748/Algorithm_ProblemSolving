print('################################## WELCOME ######################################')
name=input('이름이 뭔가요?:')
new_id=input('아이디를 설정해주세요')
print('사용할 수 있는 아이디 입니다')
birthday=input('생일을 입력해주세요(예:0717)')

play=True
while play:
    useable = True
    tmp_pw=input('원하는 비밀번호를 입력하세요')

    if len(tmp_pw)<8:
        useable=False
        print('비밀번호는 최소 8글자여야합니다')

    for i in range(len(new_id)-2):
        if new_id[i:i+3] in tmp_pw:
            print('아이디와 3자이상 중복됩니다')
            useable=False
            break

    if birthday in tmp_pw:
        useable=False
        print('생일이 비밀번호에 포함됩니다')

    special='!?*^'
    special_tmp=False
    for s in special:
        if s in tmp_pw:
            special_tmp=True
            break

    if not special_tmp:
        print('!?*^ 중 하나의 특수문자를 포함해야합니다')
        useable=False

    if useable:
        print('사용할 수 있는 비밀번호입니다')
        play=False
    else:
        print('사용할 수 없는 비밀번호입니다')

play=True
while play:
    check_pw=input('비밀번호를 다시한번 입력해주세요')
    if tmp_pw==check_pw:
        play=False
    else:
        print('비밀번호랑 다릅니다')

print('############################{}({})님 회원가입 완료!##############################'.format(name, new_id))