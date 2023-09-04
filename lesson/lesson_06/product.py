class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        if self.is_on_sale:
            on_sale_string = "(on sale)"
        else:
            on_sale_string = "(not on sale)"
        return f"{self.name}, ${self.price:.2f}, {on_sale_string}"

    def __repr__(self):
        return str(self)

    def put_on_sale(self, discount_percentage):
        """Put Product on sale by discount_percentage as decimal (e.g., 0.2 is 20% off)."""
        self.price *= (1 - discount_percentage)
        self.is_on_sale = True


class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"


"""
class Taxi(Car):
    price_per_km = 1.23
    def __init__(self, name, fuel):
"""

print(__name__)

if __name__ == '__main__':
    p = Product("Phone", 340, False)
    print(p.name, "...")
    print(p)
    p.put_on_sale(0.1)
    print(p)
    p.__bad = False
    p.x = 1

