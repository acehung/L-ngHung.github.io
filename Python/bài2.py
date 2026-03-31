import unittest


def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        # Các số nguyên tố kỳ vọng trả về True
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))

    def test_non_prime_numbers(self):
        # Các số không phải số nguyên tố kỳ vọng trả về False
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(18))
    if __name__ == '__main__':
        unittest.main()