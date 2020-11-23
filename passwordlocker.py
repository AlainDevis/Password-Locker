import datetime

class User:
    """
    class for defining the password locker object 
    """
    
    def __init__(self,username,password):
        '''
        defining the User class attributes
        '''
        self.username = username
        self.password = password
    
    def check(self):
        '''
        method designed to check if you entered 
        the correct credential while login in and 
        direct you to the menu to choose the operation to perform
        '''
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
                print("--------------------------------------------------------------------------")
                print("please fill again your password locker credential to choose another option")
                self.check()
            elif (self.choice == '2'):
                self.usercredentials = Credentials()
                self.usercredentials.view() 
                print("--------------------------------------------------------------------------")
                print("please fill again your password locker credential to choose another option")
                self.check()
            elif (self.choice == '3'):
                self.usercredentials = Credentials()
                self.usercredentials.create()  
                print("--------------------------------------------------------------------------")
                print("please fill again your password locker credential to choose another option")
                self.check()    
            elif (self.choice == '4'):
                self.usercredentials = Credentials()
                self.usercredentials.delete()  
                print("--------------------------------------------------------------------------")
                print("please fill again your password locker credential to choose another option")
                self.check()        
            else:
                 exit()
        else:
            print("invalid username or password")

class Credentials:
    """
    a class to help you perform different operation like
    Store existing,creating new credentials, view or delete 
    """
    user_list = []
    # def __init__(self,account_name,username,password):
    #     """
    #     """
    #     self.account_name = account_name
    #     self.username = username
    #     self.password = password
    
    def store(self):
        '''
        method to help storing the existing credentials 
        '''
        self.acc_credential = []
        print("Enter the existing account name like twitter")
        acc =input()
        self.acc_credential.append(acc)
        print("Enter the existing username of your account")
        acc_username =input()
        self.acc_credential.append(acc_username)
        print("Enter the existing password of your account")
        acc_password =input()
        self.acc_credential.append(acc_password)
        self.user_list.append(self.acc_credential)
        # print(self.user_list)

    def view(self):
        '''
        method to help view stored credentials 
        '''
        print("Your Credentials")
        if len(self.user_list)==0:
            print("no any stored credentials")
        for i in range(len(self.user_list)):
             print(self.user_list[i])
    
    def create(self):
        '''
        method to help create the new credentials 
        '''
        self.new_credential = []
        print("Enter the new account name ")
        new_acc =input()
        self.new_credential.append(new_acc)
        print("Enter the username of your new account")
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
    def delete(self):
        '''
        method to help delete the credentials 
        '''
        if len(self.user_list)==0:
            print("no any stored credentials")
        else:
            index=0
            for i in range(len(self.user_list)): 
                print("press %d to delete %s" %(index,self.user_list[i]))
                index=index+1
            print("choose which one to delete")
            delchoice = int(input())
            del self.user_list[delchoice]
           

userinfo = User("alain","devis123")
userinfo.check()

