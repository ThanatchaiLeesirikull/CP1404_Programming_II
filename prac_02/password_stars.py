"""
def function

    set MINIMUM_LENGTH to 12

    get password

    error_checking(password, MINIMUM_LENGTH)

    password_stars = get_password(password)

    print password_stars


def function

    while len(password) < minimum_length
        print invalid statement
        get password


def function

    return '*' * len(password)


main()
"""


def main():
    """get password and print stars"""

    MINIMUM_LENGTH = 12

    password = input("Enter password: ")

    error_checking(password, MINIMUM_LENGTH)

    password_stars = get_password(password)

    print(password_stars)


def error_checking(password, minimum_length):
    """ensuring that the input meet minimum length requirement"""

    while len(password) < minimum_length:
        print("Invalid")
        password = input("Enter password: ")


def get_password(password):
    """print the length of password into stars"""

    return '*' * len(password)


main()