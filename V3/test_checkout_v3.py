import unittest
from checkout_v3 import sum_checkout

class TestCheckout(unittest.TestCase):

    def test_sum_checkout(self):
        items = [50, 30]
        self.assertEqual(sum_checkout(items), 80)

if __name__ == '__main__':
    unittest.main()
