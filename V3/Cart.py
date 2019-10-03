class Cart():

    def __init__(self):
        self.items = []
        self.total_items = {}
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items

    def list_total_items(self):
        for item in self.items:
            if item in self.total_items:
                self.total_items[item] += 1
            else:
                self.total_items[item] = 1
        return self.total_items

    def check_offers(self, offers):
        total_items = self.total_items
        for item in total_items:
            if item in offers:
                while self.total_items[item] >= offers[item]["units"]:
                    self.total_price += offers[item]["price"]
                    self.total_items[item] -= offers[item]["units"]
        return self.total_price

    def sum_items(self, prices):
        for item in self.total_items:
            if item in prices:
                self.total_price += prices.get(item)
        return self.total_price
