from receipt import Receipt

r = Receipt("ShopWithUs")
r.add_item("Bread", 18.50, 2)
r.add_item("Milk 2L", 34.99)
r.add_item("Eggs (18)", 62.00)

r.print_slip(cash=200)