import unittest
import requests # type: ignore
from unittest.mock import patch, MagicMock

def fetch_user():
    response = requests.get("https://api.example.com/user")
    return response.json()

class TestAPI(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_user_success(self, mock_get):
        # Tạo một object giả lập cho response trả về
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": 1, "name": "Gemini"}
        
        # Gán response giả này cho hàm requests.get đã được mock
        mock_get.return_value = mock_response
        
        # Thực thi hàm
        result = fetch_user()
        
        # Kiểm tra kết quả
        self.assertEqual(result["name"], "Gemini")
        # Đảm bảo requests.get đã được gọi đúng URL
        mock_get.assert_called_once_with("https://api.example.com/user")
if __name__ == '__main__':
    unittest.main()