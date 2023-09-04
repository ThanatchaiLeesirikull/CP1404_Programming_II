from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
year = int(input("Year: "))
cost = float(input("Cost: $"))

print(f"{name} ({year}) : ${cost} added.")

print()
print("Name:")
print()
print("... snip ...")
print()

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
guitars.append(Guitar(name, year, cost))

print("These are my guitars: ")
for i, guitar in enumerate(guitars, 1):
    vintage_status = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_status}")
