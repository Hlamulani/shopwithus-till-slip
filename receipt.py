class Item:

    def __init__ (self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def line_totatl(self):
        return self.price * self.quantity