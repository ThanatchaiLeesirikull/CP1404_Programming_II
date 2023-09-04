#pseudocode
"""
total = 0
OUT_RANGE_NUMBER = 100
DISCOUNT = 0.9

get items_amount

while items_amount < 0
    print "Invalid number of items"
    get items_amount

for i in range(items_amount)
    get item_price

    total += item_price

if total > OUT_RANGE_NUMBER
    total *= DISCOUNT

print items_amount, total
"""

total_price = 0
OUT_RANGE_NUMBER = 100
DISCOUNT = 0.9

items_amount = int(input("Number of items: "))

while items_amount < 0:
    print("Invalid number of items")
    items_amount = int(input("Number of items: "))

for i in range(items_amount):
    item_price = float(input("Price of item: "))

    total_price += item_price

if total_price > OUT_RANGE_NUMBER:
    total_price *= DISCOUNT

print(f"Total price for {items_amount} items is ${total_price:.2f}")

