from user import Users
from process import process
if __name__ == '__main__' :
    globals()['user_now'] = "未登入"
    flag = 0
    while flag == 0:
        print("==================================================================")
        print(f"目前身份為:{globals()['user_now']}")
        print("==================================================================")
        flag = process(flag)
        
