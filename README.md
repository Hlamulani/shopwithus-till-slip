# ShopWithUs Till Slip

A command-line till slip generator written in Python. Built to practise
object-oriented programming, string formatting and file handling.

## Features
- Enter items with price and quantity
- Aligned, till-style slip using f-string format specifiers
- VAT (15%) calculated from VAT-inclusive prices
- Cash and change calculation with input validation
- Each slip is saved as a timestamped `.txt` file
- Unit tests with `unittest`

## Project structure
```
shopwithus-till-slip/
├── main.py                  # interactive program
├── receipt.py               # Item and Receipt classes
├── tests/test_receipt.py    # unit tests
├── .gitignore
└── README.md
```

## Run it
```
python main.py
```

## Run the tests
```
python -m unittest discover tests
```

## Example output
```
                 SHOPWITHUS
            2026-11-07 18:20:48
--------------------------------------------
ITEM                                   PRICE
--------------------------------------------
1 x Soft-drink Coca-cola 1.5L         R21.99
1 x Kellogg's Corn Flakes 1kg         R79.00
3 x Crunch berry Lunchbar 300g        R44.97
2 x Meat & Steak Pie                  R40.00
1 x Cup cakes Vanilla                 R25.00
--------------------------------------------
VAT (15% incl.)                       R27.52
TOTAL                                R210.96
CASH                                 R250.00
CHANGE                                R39.04
--------------------------------------------
          Thank you for shopping!
```
```

## Next steps
- Load a product catalogue from a CSV file
- Add discounts and card payments
- Export slips to PDF with a logo
- Store sales in SQLite and analyse them with pandas