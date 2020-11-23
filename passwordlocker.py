class User:
    """
    """
    
    def __init__(self,username,password):
        '''
        '''
        self.username = username
        self.password = password
    
    def check(self):
        print("Enter username")
        self.u = input()
        print("Enter password")
        self.p = input()
        if (self.u == self.username and self.p == self.password):
            self.usercredentials = Credentials()
            self.usercredentials.store()
        else:
            print("invalid username or password")

class Credentials:
    """
    """
    user_list = []
    # def __init__(self,account_name,username,password):
    #     """
    #     """
    #     self.account_name = account_name
    #     self.username = username
    #     self.password = password
    
    def store(self):
        self.acc_credential = []
        print("Enter the account name like twitter")
        acc =input()
        self.acc_credential.append(acc)
        print("Enter the username of your account")
        acc_username =input()
        self.acc_credential.append(acc_username)
        print("Enter the password of your account")
        acc_password =input()
        self.acc_credential.append(acc_password)
        self.user_list.append(self.acc_credential)
        print(self.user_list)

    def 


userinfo = User("alain","devis123")
userinfo.check()

