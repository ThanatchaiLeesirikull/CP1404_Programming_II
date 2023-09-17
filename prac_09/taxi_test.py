from prac_09.taxi import Taxi


def main():
    taxi_test = Taxi("Prius 1", 100)
    taxi_test.drive(40)

    print(f"{taxi_test} \nThe current fare is {taxi_test.get_fare()}")

    taxi_test.start_fare()
    taxi_test.drive(100)

    print(f"{taxi_test} \nThe current fare is {taxi_test.get_fare()}")


if __name__ == "__main__":
    main()
