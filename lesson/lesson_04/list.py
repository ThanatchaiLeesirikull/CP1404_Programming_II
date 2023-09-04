# things = ["one"]

# print(things[1])

# practice 1
"""
names = ["Benz", "Tarshan", "David", "Sky", "Gunty"]

is_finished = False
while not is_finished:
    try:
        names_order = int(input("Enter: "))
        print(names[names_order])
        is_finished = True

    except ValueError:
        print("Number must be valid")

    except IndexError:
        print("Order must be valid")
print("Finished.")
"""

"""
numbers = [1, 2, 3, 4, 5]

del numbers[-1]

numbers.remove(2)

numbers.append(2.5)

numbers.count(1)

numbers.reverse()

print(numbers)
"""

"""
def main():
    numbers = [1, 2, 3]
    add_offset(numbers, 2)
    print(numbers)


def add_offset(elements, offset):
    for i in range(len(elements)):
        elements[1] += offset


main()
"""

things = [["Benz", "Tarshan", "Woo"], [1, 2, 3], 'a']

print(things[1][2])


from operator import itemgetter

data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
# data.sort()
data.sort(key=itemgetter(1)) # reverse=True
for record in data:
    print(record)


"""
words = 'one two three'.split()
for i in range(len(words)): # capitalise each word
    words[i] = words[i].title()
text = ', '.join(words) # put commas between words
print(text)
"""

"""
string = "Hello"
print(string[0]) # 'H'

for character in string:
    print(character.upper(), end="-")
print(len(string))
"""

"""
score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]

round_trip = int(input("Enter: "))

for i in range(1, round_trip + 1):
    name = input("User Name: ")
    number = int(input("User Number: "))
    score_pairs.append([name, number])

score_pairs.sort(key=itemgetter(1), reverse=True)

for data in score_pairs:
    print(data)
"""

"""
def get_low_high(values):
    return min(values), max(values)


things = [4, -12, 7, 15, 0]

x, y = (1, 2)  # (1, 2) is a tuple
print(x, type(x))  # Output: 1 <class 'int'>

low, high = get_low_high(things)
print(low, type(low))  # Output: -12 <class 'int'>

z = get_low_high(things)
print(z, type(z))  # Output: (-12, 15) <class 'tuple'>
"""

"""
def format_date(day, month, year):
    return f"{day}/{month}/{year}"


date = (22, 11, 1988)
format_date(*date)
"""

"""
data = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
numbers = [10, 0, -3, 50, -32, 64, 99, 200]
words = "CP1404 is a very good subject and I am HAPPY".split()
"""

"""
date_string = input("Enter DOB (d/m/y): ")
parts = date_string.split("/") # this will be a list of strings
my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
"""

"""
[x + y for x in range(1, 4) for y in range(1, 4)]

things = []
    for x in range(1, 4):
        for y in range(1, 4):
            things.append(x + y)
"""


text = "This is a sentence".split()

long_word = [word for word in text if len(word) > 3]

print(long_word)


text = "This is a sentence"

words = text.split()

long_word = [word for word in words if len(word) > 3]

print(long_word)

# Pytho
#
# Py
# Pyt
# hon


def main():
    string = "?name=Bob&age=99&day=Wed"

    pairs = extract_pairs(string)
    result = [('name', 'Bob'), ('age', 99), ('day', 'Wed')]
    assert pairs == result
    print(pairs)


def extract_pairs(string):
    """Extract name-value pairs as tuples in a list from a query string."""
    if not string.startswith('?'):
        return []
    pairs = []
    parts = string[1:].split('&')
    for part in parts:
        pair = part.split('=')
        try:
            pairs.append((pair[0], int(pair[1])))
        except ValueError:
            pairs.append((pair[0], pair[1]))
    return pairs


main()

names = ["Dior", "Chanel"]

print(names[0], names[1])

"""
string = "?name=Bob&age=99&day=Wed"

name = string[1:].split('&')

for word in name:
    print(tuple(word.split('=')), end="")
"""

string = "?name=Bob&age=99&day=Wed"

words = []

for i in range(len(string)):
    tuple_words = (tuple(string[i].split("=")))
    print(tuple_words)
    words.append(tuple(tuple_words))

print(words)
