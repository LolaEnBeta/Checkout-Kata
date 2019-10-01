import unittest

class TestCheckout(unittest.TestCase):

    def test_sum_checkout(self):
        items = [50, 30]
        total_price = (items[0] + items[1])
        self.assertEqual(total_price, 80)

if __name__ == '__main__':
    unittest.main()
