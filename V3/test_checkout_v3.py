import unittest
from Cart import Cart

class TestCheckout(unittest.TestCase):

    def test_list_items(self):
        cart = Cart()
        items = cart.list_items()
        self.assertEqual(items, [])

    def test_list_total_items(self):
        cart = Cart()
        cart.add_item("A")
        items = cart.list_total_items()
        self.assertEqual(items, {"A":1})

    def test_add_item(self):
        cart = Cart()
        cart.add_item("A")
        items = cart.list_items()
        self.assertEqual(items, ["A"])

    def test_sum_items(self):
        cart = Cart()
        cart.add_item("A")
        cart.add_item("B")
        cart.list_total_items()

        prices = {"A": 50, "B": 30}
        total_price = cart.sum_items(prices)
        self.assertEqual(total_price, 80)

    def test_check_offers(self):
        cart = Cart()
        cart.add_item("A")
        cart.add_item("A")
        cart.list_total_items()

        offers = {
            "A": {
                "units": 2,
                "price": 95
            }
        }

        total_price_offers = cart.check_offers(offers)

        self.assertEqual(total_price_offers, 95)

if __name__ == '__main__':
    unittest.main()
