"""
for i range from 0 to 20 increased by 2
    print i
print
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.

"""
for i in range from 0 to 100 increased by 10
    print i
print
"""

for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b.

"""
for i in range from 20 to 0 decreased by 1
    print i
print
"""

for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c.

"""
get number_of_stars

for star in range(number_of_stars)
    print "*"
print
"""

number_of_stars = int(input("Number of stars: "))

for star in range(number_of_stars):
    print("*", end='')
print()

#d.

"""
get number_of_stars

for star in range(1, number_of_stars + 1)
    print stars
print
"""

number_of_stars = int(input("Number of stars: "))

for star in range(1, number_of_stars + 1):
    print(star * "*")
print()
