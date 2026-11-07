from receipt import Receipt, money

def ask_number(prompt, number_type=float):
    while True:
        try:
            return number_type(input(prompt))
        except ValueError:
            print("Please Enter a valid number.")

def main():
    receipt = Receipt("ShopWithUs")
    print("Enter items. Press Enter on an empty name when done.\n")

    while True:
        name = input("Item name: ").strip()
        if name == "":
            break
        price = ask_number("Price: R")
        quantity = ask_number("Quantity: ", int)
        receipt.add_item(name, price, quantity)

    if not receipt.items:
        print("No items entered.")
        return

    cash = ask_number(f"Total is {money(receipt.total())}. Cash given: R")
    while cash < receipt.total():
        print("Not enough cash.")
        cash = ask_number("Cash given: R")

    print()
    receipt.print_slip(cash)
    filename = receipt.save(cash)
    print(f"\nSaved to {filename}")

if __name__ == "__main__":
    main()