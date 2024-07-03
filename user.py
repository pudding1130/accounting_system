class Users():
    def __init__(self, name, password = None):
        self.name = name
        self.password = password
        #self.balance = 0
    def login(self):
        if self.password == None:
            print( self.name + "歡迎登入!")
        else : 
            while True:
                pwd = input(f"請輸入{self.name}的密碼")
                if pwd==self.password:
                    print("歡迎登入！")
                    break
                else:
                    print("密碼錯誤，請重新輸入")
    def pwd_set(self):
        print(f"請設定{self.name}的密碼")
        self.password = input()
    def remove(self):
        print(f"{self}已登出")
        del self
    #def update(self):
    #    while True : 
    #        try:
    #            balance = input("請輸入金額")
    #            self.balance = self.balance + int(balance)
    #            break
    #        except:
    #            print("請輸入數值")
    #    print(f"{balance}當下餘額為{self.balance}")
