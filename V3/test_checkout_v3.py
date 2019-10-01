import unittest
from checkout_v3 import sum_checkout

class TestCheckout(unittest.TestCase):

    def test_sum_checkout_items_list(self):
        items = [50, 30]
        self.assertEqual(sum_checkout(items), 80)

    def test_sum_checkout_items_dictionary(self):
        items = {"A": 50, "B": 30}
        total_price = items["A"] + items["B"]
        self.assertEqual(total_price, 80)

if __name__ == '__main__':
    unittest.main()
