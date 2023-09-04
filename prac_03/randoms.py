import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

print(random.randint(1, 100))

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

1. 5 is the smallest number and 20 is the largest number.
"""

"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

2. 3 is the smallest number and 9 is the largest number
   line 2 program could not produce 4 as the every sequence appear as an odd number.
"""

"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

3. 2.5 number is the smallest number and 5.5 is the largest number
"""
