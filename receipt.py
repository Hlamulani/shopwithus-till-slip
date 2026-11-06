class Item:

    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def line_total(self):
        return self.price * self.quantity


class Receipt:

    def __init__(self, store_name):
        self.store_name = store_name
        self.items = []

    def add_item(self, name, price, quantity=1):
        item = Item(name, price, quantity)
        self.items.append(item)

    def total(self):
        total = 0
        for item in self.items:
            total += item.line_total()
        return total