import random

MINIMUM_BORN_RATE = 0.1
MAXIMUM_BORN_RATE = 0.2
MINIMUM_DEATH_RATE = 0.05
MAXIMUM_DEATH_RATE = 0.25


def main():

    total_population = 1000
    year = 1
    ten_year_period = 10

    print("Welcome to the Gopher Population Simulator")

    for i in range(ten_year_period):

        born_gopher = calculate_born_gopher(total_population)
        death_gopher = calculate_death_gopher(total_population)

        print(f"{born_gopher:.0f} gophers were born. {death_gopher:.0f} died.")
        print(f"Population: {total_population:.0f}")
        print(f"Year {year}")

        total_population += born_gopher
        total_population -= death_gopher
        year += 1


def calculate_death_gopher(total_population):
    death_gopher_rate = random.uniform(MINIMUM_DEATH_RATE, MAXIMUM_DEATH_RATE)
    death_gopher = death_gopher_rate * total_population
    return death_gopher


def calculate_born_gopher(total_population):
    born_gopher_rate = random.uniform(MINIMUM_BORN_RATE, MAXIMUM_BORN_RATE)
    born_gopher = born_gopher_rate * total_population
    return born_gopher


main()
