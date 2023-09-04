name_to_age = {"Bill": 61, "Benz": 34, "David": 56}
flowers = ("cala lily", "rose", "tulip", "tulip")
numbers = (23, 45, 60, 60)

print({key: value * 2 for (key, value) in name_to_age.items()})

print({key: value for (key, value) in name_to_age.items() if value == max(name_to_age.values())})

print({key: value for (key, value) in name_to_age.items() if value > 20})

print(dict(zip(flowers, numbers)))
print(list(zip(flowers, numbers)))
print(tuple(zip(flowers, numbers)))
print(set(zip(flowers, numbers)))
