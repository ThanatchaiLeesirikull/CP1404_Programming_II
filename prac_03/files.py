# Write code that asks the user for their name, then opens a file called "name.txt" and \
# writes that name to it. Remember to close your file.

name = input("Name: ")

out_file = open("name.txt", "w")

print(name, file=out_file)

out_file.close()

# (In the same file, but as if it were a separate program) Write code that opens "name.txt"
# and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in file).

in_file = open("name.txt", "r")

stored_name = in_file.readline().strip()

in_file.close()

print(f"Your name is {stored_name}")

# 3.

in_file = open("numbers.txt", "r")

total = 0

for i in range(2):
    line = in_file.readline().strip()
    print(line)

    total += int(line)

in_file.close()

print(f"The sum of the first two line is {total}")

in_file = open("numbers.txt", "r")

total = 0

for line in in_file:
    line = line.strip()
    if line.isdigit():
        total += int(line)

in_file.close()

print(f"Total sum for all lines is {total}")
