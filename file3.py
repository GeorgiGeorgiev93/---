class Car:
    def __init__(self, brand, speed, registration):
        self.brand = brand
        
        self._speed = speed
        
        self.__registration = registration

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self._speed} km/h")
        print(f"Secret Code (masked): {self.__mask_secret()}")

    def _increase_speed(self, amount):
        self._speed += amount

    def _decrease_speed(self, amount):
        self._speed -= amount

    def __mask_secret(self):
        return "***" + self.__registration[-2:]

    def reveal_secret(self):
        return self.__registration


car = Car("Honda", 100, "OB4837BA")

print(car.brand)

print(car._speed)

try:
    print(car.__registration)
except AttributeError:
    print("Cannot access private field directly!")

print(car._Car__registration)

car.show_info()
car._increase_speed(10)
print("New speed:", car._speed)