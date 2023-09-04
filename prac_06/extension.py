class Car:

    def __init__(self, name="", fuel=0, odo=0):
        self.name = name
        self.fuel = fuel
        self.odo = odo

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odo}"

    def drive_in_km(self, drive):
        if drive < 0:
            print("Distance must be >= 0")
        elif drive <= self.fuel:
            self.fuel -= drive
            self.odo += drive
            print(f"The car drove {drive} km.")
        else:
            print("Not enough fuel to drive that distance.")


def main():

    print("Let's drive!")
    name = input("Enter your car name: ")

    car = Car(name, 100, 0)
    print(f"{car.name}, fuel={car.fuel}, odo={car.odo}")

    menu = (
        "Menu:\n"
        "d) drive\n"
        "r) refuel\n"
        "q) quit"
    )

    print(menu)

    choice = input("Enter your choice: ").upper()

    while choice != "Q":
        if choice == "D":
            drive = int(input("How many km do you wish to drive? "))
            car.drive_in_km(drive)

        elif choice == "R":
            car.odo = int(input("How many units of fuel do you want to add to the car? "))

            while car.odo < 0:
                print("Fuel amount must be >= 0")
                car.odo = int(input("How many km do you wish to drive? "))

            print(f"Added {car.odo} units of fuel.")

        else:
            print("Invalid choice")

        print(f"{car.name}, fuel={car.fuel}, odo={car.odo}")
        choice = input("Enter your choice: ").upper()


main()
