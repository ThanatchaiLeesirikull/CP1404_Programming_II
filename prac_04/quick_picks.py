import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS = 6


def main():
    """program to pick up the random number and sort the number"""

    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUM_PICKS):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join(f"{number:2}" for number in quick_pick))


main()
