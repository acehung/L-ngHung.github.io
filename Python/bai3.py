import unittest

class User:
    def __init__(self, username):
        self.username = username
    
    def is_admin(self):
        return self.username == "admin"

class TestUser(unittest.TestCase):
    def test_admin_user(self):
        user = User("admin")
        self.assertTrue(user.is_admin())

    def test_guest_user(self):
        user = User("guest")
        self.assertFalse(user.is_admin())

    def test_normal_user(self):
        user = User("user123")
        self.assertFalse(user.is_admin())
if __name__ == '__main__':
    unittest.main()