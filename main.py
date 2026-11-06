from receipt import Receipt

r = Receipt("ShopWithUs")
r.add_item("Bread", 18.50, 2)
r.add_item("Milk 2L", 34.99)

print(len(r.items))
print(f"{r.total():.2f}")