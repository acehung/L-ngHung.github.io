import unittest


def clean_input(s):
    return s.strip().lower().replace(" ", "_")

class TestStringProcessing(unittest.TestCase):
    def test_clean_input_basic(self):
        # Test với chuỗi có khoảng trắng, chữ hoa
        self.assertEqual(clean_input("  Hello World  "), "hello_world")

    def test_clean_input_multiple_spaces(self):
        # Lưu ý: replace(" ", "_") chỉ thay 1-1, 
        # nếu có 2 dấu cách sẽ thành 2 dấu gạch dưới
        self.assertEqual(clean_input("Python   Is   Fun"), "python___is___fun")

    def test_clean_input_no_changes(self):
        # Test với chuỗi đã chuẩn hóa sẵn
        self.assertEqual(clean_input("already_clean"), "already_clean")
    def test_clean_input_empty_string(self):
        # Test với chuỗi rỗng
        self.assertEqual(clean_input(""), "")