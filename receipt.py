from datetime import datetime

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
        self.timestamp = datetime.now()

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

    def render(self, cash=None):
        width = 40
        line = "-" * width
        date_text = f"{self.timestamp:%Y-%m-%d %H:%M:%S}"

        lines = [
            f"{self.store_name.upper():^{width}}",
            f"{date_text:^{width}}",
            line,
            f"{'ITEM':<28}{'PRICE':>12}",
            line,
        ]

        for item in self.items:
            label = f"{item.quantity} x {item.name}"
            lines.append(f"{label:<28}{money(item.line_total()):>12}")

        lines.append(line)
        lines.append(f"{'VAT (15% incl.)':<28}{money(self.vat()):>12}")
        lines.append(f"{'TOTAL':<28}{money(self.total()):>12}")

        if cash is not None:
            lines.append(f"{'CASH':<28}{money(cash):>12}")
            lines.append(f"{'CHANGE':<28}{money(cash - self.total()):>12}")

        lines.append(line)
        lines.append(f"{'Thank you for shopping!':^{width}}")
        return "\n".join(lines)

    def print_slip(self, cash=None):
        print(self.render(cash))

    def save(self, cash=None):
        filename = f"receipt_{self.timestamp:%Y%m%d_%H%M%S}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.render(cash))
        return filename