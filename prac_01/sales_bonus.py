"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

#pseudo code
"""
OUT_RANGE_NUMBER = 1000
OUT_RANGE_BONUS = 0.15
IN_RANGE_BONUS = 0.1

get sales

while sales >= 0

    if sales >= OUT_RANGE_NUMBER
        percentage = OUT_RANGE_BONUS
    else
        percentage = IN_RANGE_BONUS
        
    calculate bonus
    
    print bonus
    
    get sales
"""

OUT_RANGE_NUMBER = 1000
OUT_RANGE_BONUS = 0.15
IN_RANGE_BONUS = 0.1

sales = float(input("Enter sales: $"))

while sales >= 0:

    if sales >= OUT_RANGE_NUMBER:
        percentage = OUT_RANGE_BONUS
    else:
        percentage = IN_RANGE_BONUS

    bonus = sales * percentage

    print(f"The bonus is ${bonus}")

    sales = float(input("Enter sales: $"))
