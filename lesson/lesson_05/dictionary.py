def main():

    name_to_age = {"David": 0, "Jane": 4, "Sven": 56}
    names = ['Benz', 'Bam', 'Bamboo', 'Max']
    ages = [12, 134, 56, 0]

    print(name_to_age.values())
    print(name_to_age.keys())
    print(name_to_age.items())
    print(max(name_to_age.values()))

    for i in range(len(name_to_age)):
        print(i)

    for i in name_to_age:
        print(f"{i} - {name_to_age[i]}")

    name = input("Name: ")
    age = input("Age: ")
    name_to_age[name] = age
    max_length = max(len(name) for name in list(name_to_age.keys()))

    print(print_statement(name_to_age, max_length))
    print(find_oldest(names, ages))


def print_statement(name_to_age, max_length):
    for name, age in name_to_age.items():
        print(f"{name:{max_length}} -\t{age:3}")


def find_oldest(names, ages):
    # return names[ages.index(max(ages))]
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names[oldest_index]


main()


name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
for name in name_to_age:
    print(f"{name} is {name_to_age[name]}")

ages = list(name_to_age.values())
ages.sort()
print(ages)

word_to_count = {"apple": 8, "Kiwi": 4}
words = ["apple", "orange"]

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
    print(word, word_to_count[word])