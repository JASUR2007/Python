    # db_log=['admin','user']
    # db_pass=['1234','qwerty']
    # flag = True
    # attempts = 3
    # n = 0
    # while flag:
    #     login = input('Login ')
    #     password = input('Pass ')
    #     if login in db_log and password in db_pass:
    #         print("Welcome!")
    #         flag = False
    #     else:
    #         print('Incorrect login or password. Try again!')
    #         n = n + 1
    #         if n == attempts:
    #             flag = False



user_list = {'user':{'login':'admin','password':'12345'},
             'agent':{'login':'agent007','password':'qwerty'}}
flag = True
attempts = 3
n = 0
while flag:
    login = input('Login ')
    password = input('Pass ')
    for i in user_list:
        if login in user_list[i]['login'] and password in user_list[i]['password']:
            print("Welcome!", i)
            flag = False
            break
    else:
        print('Incorrect login or password. Try again!')
        n = n + 1
        if n == attempts:
            flag = False
            break

