class CarRecord:

    def __init__(self, brand="", price=0.0, colour="", speed=1):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.speed = speed

    def __str__(self):
        """Return a descriptive string for this instance, involved by print() and str()"""
        return f"I am driving a {self.brand} car in {self.colour} colour. It cost {self.price:,.2f}. The accelerate\nspeed is {self.get_break()}"

    def get_break(self):
        return self.speed + 1


def main(cars):
    car_brand = input("Enter car brand: ")
    car_colour = input("Enter car colour: ")
    car_price = float(input("Enter car price: "))
    car_speed = int(input("Enter car speed: "))

    car2 = CarRecord(car_brand, car_price, car_colour, car_speed)

    cars.append(car2)

    car3 = CarRecord()