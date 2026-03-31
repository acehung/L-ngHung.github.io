import unittest
from unittest.mock import patch
from datetime import datetime

# Hàm cần test
def is_weekend():
    today = datetime.now().weekday()
    return today >= 5

class TestWeekend(unittest.TestCase):
    @patch('datetime.datetime')
    def test_is_weekend_friday(self, mock_datetime):
        # Giả lập là Thứ 6 (weekday = 4)
        mock_datetime.now.return_value.weekday.return_value = 4
        self.assertFalse(is_weekend())

    @patch('datetime.datetime')
    def test_is_weekend_saturday(self, mock_datetime):
        # Giả lập là Thứ 7 (weekday = 5)
        mock_datetime.now.return_value.weekday.return_value = 5
        self.assertTrue(is_weekend())
    @patch('datetime.datetime')
    def test_is_weekend_sunday(self, mock_datetime):
        # Giả lập là Chủ Nhật (weekday = 6)
        mock_datetime.now.return_value.weekday.return_value = 6
        self.assertTrue(is_weekend())