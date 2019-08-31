import unittest
from util.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Method to run before each test case
        """
        self.new_user = User('victor', 'vick3445!')  # Create user object

    def tearDown(self):
        """
        Clear contact_list
        """
        self.user_list = []  # Clear user_list

    def test__init__(self):
        """
        Check is class was init
        """
        self.assertEqual(self.new_user.name, "victor")
        self.assertEqual(self.new_user.password, "vick3445!")

    def test_save_user(self):
        """
        Check is the user list is incremented
        """
        self.new_user.save_user()
        self.assertEqual(User.user_list.__len__(), 6)

    def test_save_multiple_user(self):
        """
        Check saving for > 1 user
        """
        self.new_user.save_user()
        test_new = User("Kamau", "password")
        test_new.save_user()
        self.assertEqual(User.user_list.__len__(), 5)

    def test_delete_user(self):
        """
        Test deleting a user
        """
        self.new_user.save_user()
        test_new = User("Kamau", "password")
        test_new.save_user()
        self.new_user.del_user()
        self.assertEqual(len(User.user_list), 3)

    def test_check_user(self):
        """
        Find if a user exists
        """
        self.new_user.save_user()
        test_new = User("Kamau", "password")
        test_new.save_user()
        found_user = User.check_user('victor')
        self.assertEqual(found_user.name, self.new_user.name)


if __name__ == '__main__':
    unittest.main()
