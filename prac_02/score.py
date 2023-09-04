"""
import random


def function

    get score

    set random_score to get random.randint(0, 100)

    random_grade = determine_status(random_score)

    grade = determine_status(score)

    print score, grade
    print random_score, random_grade


def function

    if (score < 0) or (score > 100)
        return "Invalid score"

    elif score >= 90
        return "Excellent"

    elif score >= 50
        return "Passable"

    else
        return "Bad"


main()
"""


import random


def main():
    """get score and calculate status"""

    score = int(input("Enter score: "))

    random_score = random.randint(0, 100)

    random_grade = determine_status(random_score)

    grade = determine_status(score)

    print(f"{score} is {grade}")
    print(f"{random_score} is {random_grade}")


def determine_status(score):
    """determine status base on score"""

    if (score < 0) or (score > 100):
        return "Invalid score"

    elif score >= 90:
        return "Excellent"

    elif score >= 50:
        return "Passable"

    else:
        return "Bad"


main()
