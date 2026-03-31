import unittest


def is_strong(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

class TestPassword(unittest.TestCase):
    def test_strong_password(self):
        self.assertTrue(is_strong("SecurePass123"))

    def test_weak_password_short(self):
        # Có số nhưng quá ngắn
        self.assertFalse(is_strong("Short1"))

    def test_weak_password_no_digit(self):
        # Đủ dài nhưng không có số
        self.assertFalse(is_strong("NoDigitsHere"))

    def test_weak_password_empty(self):
        self.assertFalse(is_strong(""))
    def test_weak_password_only_digits(self):
        # Chỉ có số nhưng đủ dài
        self.assertFalse(is_strong("12345678"))