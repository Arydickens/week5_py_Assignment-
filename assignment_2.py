class Car:
    def move(self):
        print("Driving 🚗")


class Plane:
    def move(self):
        print("Flying ✈️")


class Boat:
    def move(self):
        print("Sailing 🚢")


class Bicycle:
    def move(self):
        print("Pedaling 🚴")


# List of different transport modes
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Call move() for each
for vehicle in vehicles:
    vehicle.move()
