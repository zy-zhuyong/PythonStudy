# if ... else 条件控制
def account_login():
    password = input('Password:')
    if password == '12345':
        print('Login success!')
    else:
        print('Worong password or invaiid input!')
        account_login()
account_login()

