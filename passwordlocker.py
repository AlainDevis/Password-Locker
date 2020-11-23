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
            print("correct credentials")
        else:
            print("invalid username or password")

class Credentials:
    """
    """
    user_list = []
    def __init__(self,account_name,username,password):
        """
        """
        self.account_name = account_name
        self.username = username
        self.password = password
    
    def store(self):
        print("Enter the account name like twitter")
        acc =input()
        print("Enter the username of your account")
        acc_username =input()
        print("Enter the password of your account")
        acc_password =input()



userinfo = User("alain","devis123")
userinfo.check()

