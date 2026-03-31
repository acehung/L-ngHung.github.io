def get_fruits():
    # Hàm này trả về một List các chuỗi
    return ["apple", "banana", "cherry"]
import unittest

class TestFruits(unittest.TestCase):
    
    def test_fruit_exists(self):
        """Kiểm tra các trái cây có trong danh sách"""
        fruits = get_fruits()
        
        # Kiểm tra 'apple' có trong danh sách không
        self.assertIn("apple", fruits, "Lỗi: apple phải có trong danh sách")
        
        # Kiểm tra 'banana' có trong danh sách không
        self.assertIn("banana", fruits)

    def test_fruit_not_in_list(self):
        """Kiểm tra một trái cây không tồn tại trong danh sách"""
        fruits = get_fruits()
        
        # Kỳ vọng 'orange' không có trong danh sách trả về
        self.assertNotIn("orange", fruits, "Lỗi: orange không được phép có trong danh sách")

    def test_list_length(self):
        """(Nâng cao) Kiểm tra số lượng phần tử trong danh sách"""
        fruits = get_fruits()
        self.assertEqual(len(fruits), 3)