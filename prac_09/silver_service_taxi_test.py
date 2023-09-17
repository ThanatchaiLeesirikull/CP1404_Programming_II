"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class tests
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    silver_service_taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(f"The fare is ${silver_service_taxi.get_fare()}")


main()
