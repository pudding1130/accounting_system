from user import Users
def process(flag):
    while flag == 0 :
        print("請輸入(1)建立帳戶(2)登入帳號(3)設定密碼(4)刪除帳號(5)離開系統")
        try:
            action = int(input())
            if action == 1:
                x = input("請輸入帳號")
                globals()['user_now'] = x
                globals()[x] = Users(x)
                print("帳號建立成功")
                flag = 0
                return(flag)
            if action == 2:
                x = globals()['user_now']
                globals()[x].login()
                flag = 0
                return(flag)
            if action == 3:
                x = globals()['user_now']
                globals()[x].pwd_set()
                flag = 0
                return(flag)     
            if action == 4:
                x = globals()['user_now']
                globals()[x].logout()
                flag = 0
                return(flag)
            if action == 5:
                print("Goodbye!")
                flag = 1
                return(flag)
        except:
            print("請輸入1-5")
