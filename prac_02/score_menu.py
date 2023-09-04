"""
def function

    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

    get score

    while (score < 0) or (score > 100)
        print Invalid
        get score

    print menu
    get choice

    while choice != 'Q'

        if choice == 'G'
            score = get_valid_score()

        elif choice == 'P'
            grade = determine_status(score)
            print score, grade

        elif choice == 'S'
            stars = print_stars(score)
            print stars

        else
            print invalid statement

        print menu
        get choice

    print farewell


def function

    get score

    while (score < 0) or (score > 100)
        print invalid statement
        get score =

    return score


def function

    if (score < 0) or (score > 100)
        return "Invalid score"

    elif score >= 90
        return "Excellent"

    elif score >= 50
        return "Passable"

    else
        return "Bad"


def function

    return '*' * score


main()
"""


def main():
    """get score and calculate the score into various form"""

    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

    score = int(input("Enter score: "))

    while (score < 0) or (score > 100):
        print("Invalid")
        score = int(input("Enter score: "))

    print(menu)
    choice = input("> ").upper()

    while choice != 'Q':

        if choice == 'G':
            score = get_valid_score()

        elif choice == 'P':
            grade = determine_status(score)
            print(f"{score} is {grade}")

        elif choice == 'S':
            stars = print_stars(score)
            print(stars)

        else:
            print("Invalid")

        print(menu)
        choice = input("> ").upper()

    print("farewell")


def get_valid_score():
    """get any score in range 0-100"""

    score = int(input("Enter score: "))

    while (score < 0) or (score > 100):
        print("Invalid")
        score = int(input("Enter score: "))

    return score


def determine_status(score):
    """calculate the grade base on score"""

    if (score < 0) or (score > 100):
        return "Invalid score"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Passable"

    else:
        return "Bad"


def print_stars(score):
    """print number of score into stars"""

    return '*' * score


main()
