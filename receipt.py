VAT_RATE = 0.15


def money(amount):
    return f"R{amount:.2f}"


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

    def vat(self):
        return self.total() * VAT_RATE / (1 + VAT_RATE)

    def print_slip(self, cash=None):
        width = 40
        line = "-" * width

        print(f"{self.store_name.upper():^{width}}")
        print(line)
        print(f"{'ITEM':<28}{'PRICE':>12}")
        print(line)

        for item in self.items:
            label = f"{item.quantity} x {item.name}"
            print(f"{label:<28}{money(item.line_total()):>12}")

        print(line)
        print(f"{'VAT (15% incl.)':<28}{money(self.vat()):>12}")
        print(f"{'TOTAL':<28}{money(self.total()):>12}")

        if cash is not None:
            print(f"{'CASH':<28}{money(cash):>12}")
            print(f"{'CHANGE':<28}{money(cash - self.total()):>12}")

        print(line)
        print(f"{'Thank you for shopping!':^{width}}")