import unittest
from Cart import Cart

class TestCheckout(unittest.TestCase):

    def test_list_items(self):
        cart = Cart()
        items = cart.list_items()
        self.assertEqual(items, [])

    def test_add_item(self):
        cart = Cart()
        cart.add_item("A")
        items = cart.list_items()
        self.assertEqual(items, ["A"])

    def test_sum_items(self):
        cart = Cart()
        cart.add_item("A")

        prices = {"A": 50}
        total_price = cart.sum_items(prices)
        self.assertEqual(total_price, 50)

if __name__ == '__main__':
    unittest.main()
