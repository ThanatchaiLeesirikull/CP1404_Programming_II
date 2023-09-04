"""
CP1404/CP5632 - Practical - Suggested Solution
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "password.txt"

# open output file for writing (this creates a new file if it doesn't exist)
out_file = open(FILENAME, 'w')

price = INITIAL_PRICE
day = 0
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

# don't forget to close the file when we've finished with it
out_file.close()

def convert_str_to_int(text):
    """LBYL version."""
    if not isinstance(text, str) or not text.isdigit():
        return None
    else:
        return int(text)

def convert_str_to_int(text):
    """EAFP version."""
    try:
        return int(text)
    except ValueError:
        return None

valid_input = False
while not valid_input:
    try:
        age = int(input("Age: "))
        valid_input = True
    except ValueError:
        print("Invalid (not an integer)")
print("Next year you will be", age + 1)

try:
    number = int(input("? "))
    print(10 / number)
except ValueError:
    print("Not a valid integer")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Some other exception happened")
print("Finished")

try:
    data_file = open('solution.txt')
    print(data_file.read())
except FileNotFoundError:
    print("Stop")

with open("data.txt", "r") as in_file:
    in_file.readline()  # ignore header
    for line in in_file:
        # print(line)
        parts = line.strip().split(',')
        # print(parts)
        name = parts[0]
        age = int(parts[1])
        print(f"{name} will be {age + 1} years old next year")

with open("data_1.txt", "r") as in_file:
    in_file.readline()
    for line in in_file:
        parts_1 = line.strip().split(',')
        first_name = parts_1[0]
        last_name = parts_1[1]
        year = parts_1[2]
        money = parts_1[3]
        print(f"{first_name} {last_name}, who born in {year}, earns {money}$")

import random

MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = ""

out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
day = 0
out_file.write(f"Starting price: ${price:,.2f}\n")

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    day += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    out_file.write(f"On day {day} price is: ${price:,.2f}\n")

out_file.close()
