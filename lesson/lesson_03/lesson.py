"""Guessing game with files and exceptions"""
FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()

    while guess != secret:
        print("Guess again!")
        guess = get_valid_number()
    print("You got it!")


def get_valid_number():
    guess = -1
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess  # no problem with potential undefined variable


def load_number(filename):
    """Load integer from file filename"""
    infile = open(filename, "r")
    try:
        number = int(infile.read())
    except ValueError:
        print(f"Invalid contents in {filename}")
        number = 6
    except FileNotFoundError:
        print(f"{filename} not found")
        number = 4
    else:
        infile.close()
    return number


main()


name = input("Name: ")
out_file = open("secret_1.txt", "w")
print(name, file=out_file)
out_file.close()


