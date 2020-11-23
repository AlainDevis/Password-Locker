import unittest
from passwordlocker import User,Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("alain","devis123") 
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_User.username,"alain")
        self.assertEqual(self.new_User.password,"devis123")
    def check_test(self):
        '''
        check_test test case to test if the user object credentials
        are correct
        '''
        self.new_User.check_test() 
        self.assertEqual(len(new_User))

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    user_list =[]

    def store_test(self):
        '''
        check_test test case to test if the user object credentials
        can store the credentials
        '''
        self.new_User.append(user_list)
        self.assertEqual(len(new_User))
    
    def view_test(self):
        '''
        check_test test case to test if the user object credentials
        can view stored the credentials
        '''
        print(self.user_list[i])
        self.assertEqual(len(new_User))

if __name__ == '__main__':
    unittest.main()
