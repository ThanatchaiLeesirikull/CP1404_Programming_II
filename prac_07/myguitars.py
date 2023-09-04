from prac_07.guitar import Guitar


def main():
    """guitar list storage"""
    guitars = []

    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    guitars.sort()

    for guitar in guitars:
        print(guitar)


main()
