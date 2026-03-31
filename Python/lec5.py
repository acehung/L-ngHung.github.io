import unittest

def calculate_tax(income):
    if income < 5000:
        return 0
    elif income < 10000:
        return income * 0.1
    else:
        return income * 0.2

class TestCalculateTax(unittest.TestCase):
    def test_low_income(self):
        # Trường hợp income < 5000 (VD: 3000)
        self.assertEqual(calculate_tax(3000), 0)

    def test_medium_income(self):
        # Trường hợp income = 7000 (7000 * 0.1 = 700.0)
        self.assertEqual(calculate_tax(7000), 700.0)

    def test_high_income(self):
        # Trường hợp income = 12000 (12000 * 0.2 = 2400.0)
        self.assertEqual(calculate_tax(12000), 2400.0)
if __name__ == '__main__':
    unittest.main()