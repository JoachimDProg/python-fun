# class
class Car():
    def __init__(self, make, model, color) -> None: # -> = function annotation
        self.make =  make
        self.model = model
        self.color = color
        self.mileage = 0

    def __str__(self) -> str:
        return f"My car is a {self.color.title()} {self.make.title()} {self.model.title()} and it has {self.mileage}km"

    def update_odometer(self, mileage):
        if self.mileage > mileage:
            print("can't reduce the mileage")
        else:
            self.mileage = mileage

    def goto_town(self):
        self.mileage += 100

# inheritance
class HydrogenCar(Car):
    def __init__(self, make, model, color, water_tank) -> None:
        super().__init__(make, model, color)
        self.capacity = water_tank.capacity

    def __str__(self) -> str:
        return f"My car is a {self.color.title()} {self.make.title()} {self.model.title()}, it has {self.mileage}km and a {self.capacity}l reservoir"

    def goto_town(self): # method override
        print("it can't go to town or it will explode")

class WaterTank():
    def __init__(self, capacity) -> None:
        self.capacity = capacity

# class instances
car = Car('Toyota', 'Corolla', 'blue')
water_tank = WaterTank(30)
car2 = HydrogenCar('SuperHydro', 'car', 'white', water_tank)

print(f"new car: {car}")
car.update_odometer(2567)
print(f"add mileage car: {car}")
car.goto_town()
print(f"take a ride: {car}")

print(f"\nnew hydrogen car: {car2}")
car2.goto_town()