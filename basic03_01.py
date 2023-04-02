true = True
while true == True:
    print("-----------")
    print("0. 종료")
    print("1. 회원가입")
    print("2. 로그인")
    print("-----------")
    a = input("입력: ")
    list_user = []

    if a == "0":
        print("\n프로그램 종료")
        break
    
    elif a == "1":
        print("\n-----회원가입-----")
        list_user.insert(0, input("아이디 : "))
        list_user.insert(1, input("비밀번호 : "))
        print("\n--- 회원가입 성공!")
        continue
    
    elif a == "2":
        print("\n-----로그인-----")
        id = input("아이디 : ")
        pw = input("비밀번호 : ")
        if id == list_user[0] and pw == list_user[1]:
            print("\n--- {list_user[0]}님 환영합니다!")
        else:
            print("아이디와 비밀번호를 확인해주세요.")