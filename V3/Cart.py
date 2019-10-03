class Cart():

    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items

    def sum_items(self, prices):
        for item in self.items:
            if item in prices:
                self.total_price += prices.get(item)
        return self.total_price
