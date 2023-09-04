
"""
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]
"""

# 1. 3
# 2. 2
# 3. 1
# 4. [3, 1, 4, 1, 5, 9]
# 5. True
# 6. False
# 7. False
# 8. [3, 1, 4, 1, 5, 9, 6, 5, 3]

# In the same Python file, write statements to achieve the following:

numbers = [3, 1, 4, 1, 5, 9, 2]

# 1.

numbers[0] = "ten"

# 2.

numbers[-1] = 1

# 3.

number_after_first_two_slice = numbers[2:]

print(numbers)

print(number_after_first_two_slice)

# 4.

if 9 in numbers:
    print("9 is the element of numbers")
