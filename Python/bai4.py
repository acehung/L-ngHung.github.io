from unittest.mock import patch
import unittest

def send_welcome_email(email):
    print(f"Sending email to {email}")

class TestEmail(unittest.TestCase):
    @patch('builtins.print') # Giả lập hàm print hệ thống
    def test_send_welcome_email(self, mock_print):
        email = "luonghung040805@gmail.com"
        send_welcome_email(email)
        
        # Xác nhận hàm print đã được gọi với đúng chuỗi format
        mock_print.assert_called_with(f"Sending email to {email}")
if __name__ == '__main__':
    unittest.main()