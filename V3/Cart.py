class Cart():

    def __init__(self):
        self.items = []

    def add_to_items_list(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items
