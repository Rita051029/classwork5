
class Human:

    def __init__(self, name):
        self.name = name



class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []


    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passenger_name(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passenger")
            for name in self.passengers:
                print(name.name)
        else:
            print(f"No passenger in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mersedes")

car.add_passenger(nick)
car.add_passenger(kate)

car.print_passenger_name()
