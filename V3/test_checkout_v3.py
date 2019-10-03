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

if __name__ == '__main__':
    unittest.main()
