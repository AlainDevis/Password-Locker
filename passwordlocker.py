import datetime

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
            print(
                """
                1.Store Credentials
                2.View Credentials
                3.create Credentials
                4.Delete Credentials
                5.Exit
                """
            )   
            print("What would you like to do? ")
            self.choice=input()   
            if(self.choice == '1'):
                self.usercredentials = Credentials()
                self.usercredentials.store()  
                print("please fill again your password locker credential to choose another option")
                self.check()
            elif (self.choice == '2'):
                self.usercredentials = Credentials()
                self.usercredentials.view() 
                self.check()
            elif (self.choice == '3'):
                self.usercredentials = Credentials()
                self.usercredentials.create()  
                self.check()          
            else:
                 exit()
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
        # print(self.user_list)

    def view(self):
        print("Your Credentials")
        if len(self.user_list)==0:
            print("no any stored credentials")
        for i in range(len(self.user_list)):
             print(self.user_list[i])
    
    def create(self):
        self.new_credential = []
        print("Enter the account name like twitter")
        new_acc =input()
        self.new_credential.append(new_acc)
        print("Enter the username of your account")
        new_username =input()
        self.new_credential.append(new_username)
        print("""
            1.generate password
            2.Non generated password
        """)
        print("What would you like to do? ")
        self.choice=input() 
        if (self.choice == '1'):
            x = datetime.datetime.now()
            y = x.strftime("%Y")
            pwd = ''
            for i in range(len(new_username)):
                z = new_username[i]
                pwd = pwd + z
                if i >1:
                    break
            new_password = pwd + "$" + y
        else:
            print("Enter the password of your account")
            new_password =input()
        self.new_credential.append(new_password)
        self.user_list.append(self.new_credential)
        # print(self.user_list)


userinfo = User("alain","devis123")
userinfo.check()

