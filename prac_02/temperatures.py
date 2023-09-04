"""
def function

    menu = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"

    print menu
    get choice
    while choice != 'Q'
        if choice == 'C'
            get celsius
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print fahrenheit
        elif choice == 'F'
            # TODO: Write this section to convert F to C and display the result
            get fahrenheit
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print celsius
        else
            print Invalid option
        print menu
        get choice
    print Thank you.


def function

    return celsius * 9.0 / 5 + 32


def function

    return 5 / 9 * (fahrenheit - 32)


main()
"""


def main():
    """get celsius/fahrenheit and convert temperature"""

    menu = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"

    print(menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == 'F':
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()
