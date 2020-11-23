import unittest
from passwordlocker import User,Credentials

class TestContact(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
