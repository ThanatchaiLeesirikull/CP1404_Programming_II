from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi


def main():
    """Taxi Farewell accumulator"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None

    print("Let's drive!")

    menu = "q)uit, c)hoose, d)rive"
    print(menu)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_taxi(current_taxi, taxis)

        elif choice == "D":
            get_bill(total_bill, current_taxi)

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def get_bill(bill, current_taxi):
    """get the total bill"""
    if current_taxi:
        fare = get_fare(current_taxi)
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        bill += fare
    else:
        print("You need to choose a taxi before you can drive")
    return bill


def get_fare(current_taxi):
    """get the total fare from the parent class calculation"""
    distance = int(input(f"Drive how far with {current_taxi.name}? "))
    current_taxi.drive(distance)
    fare = current_taxi.get_fare()
    return fare


def get_taxi(current_taxi, taxis):
    """choose the taxi that want to drive"""
    choose_taxi = int(input("Choose taxi: "))
    if choose_taxi >= len(taxis):
        print("Invalid taxi choice")
    else:
        current_taxi = taxis[choose_taxi]
    return current_taxi


def display_taxis(taxis):
    """display the lists of taxi"""
    for i, taxi in enumerate(taxis, 0):
        print(f"{i} - {taxi}")


main()
