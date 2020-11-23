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





userinfo = User("alain","devis123")
userinfo.check()

