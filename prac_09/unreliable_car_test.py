from prac_09.unreliable_car import UnreliableCar


def main():
    c1 = UnreliableCar('Benz', 180, 80)  # Example: Create an UnreliableCar with 80% reliability
    print(c1)
    distance_driven = c1.drive(100)  # Try to drive 50 km
    print(f"Distance driven: {distance_driven}")


if __name__ == "__main__":
    main()
