class Cart():

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items

    def sum_items(self, prices):
        total_price = 0
        for item in self.items:
            if item in prices:
                total_price =+ prices.get(item)
        return total_price
