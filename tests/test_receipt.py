import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from receipt import Item, Receipt


class ItemTests(unittest.TestCase):

    def test_line_total(self):
        item = Item("Bread", 18.50, 2)
        self.assertAlmostEqual(item.line_total(), 37.00)


class ReceiptTests(unittest.TestCase):

    def setUp(self):
        self.receipt = Receipt("ShopWithUs")
        self.receipt.add_item("Bread", 18.50, 2)
        self.receipt.add_item("Milk 2L", 34.99)

    def test_total(self):
        self.assertAlmostEqual(self.receipt.total(), 71.99)

    def test_vat_is_the_included_portion(self):
        self.assertAlmostEqual(self.receipt.vat(), 9.39, places=2)

    def test_render_shows_change(self):
        text = self.receipt.render(cash=100)
        self.assertIn("R28.01", text)


if __name__ == "__main__":
    unittest.main()