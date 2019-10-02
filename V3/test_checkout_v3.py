import unittest
from checkout_v3 import sum_checkout, sum_checkout_items_from_dictionary
from Cart import Cart

class TestCheckout(unittest.TestCase):

    def test_sum_checkout_items_list(self):
        items = [50, 30]
        self.assertEqual(sum_checkout(items), 80)

    def test_sum_checkout_items_dictionary(self):
        items = {"A": 50, "B": 30}
        self.assertEqual(sum_checkout_items_from_dictionary(items), 80)

    def test_add_item(self):
        new_cart = Cart()
        new_cart.add_to_items_list("A")
        self.assertEqual(new_cart.list, ["A"])

if __name__ == '__main__':
    unittest.main()
