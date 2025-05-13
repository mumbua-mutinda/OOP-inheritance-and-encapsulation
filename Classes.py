class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f" Hi, I'm {self.name} from {self.origin}, and I use {self.power}!")

    def move(self):
        print(f"{self.name} moves swiftly through the city.")

##INHERITANCE
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, altitude_limit):
        super().__init__(name, power, origin)
        self.altitude_limit = altitude_limit

    # POLYMORPHISM
    def move(self):
        print(f"{self.name} soars through the skies up to {self.altitude_limit} feet!")

class SpeedHero(Superhero):
    def move(self):
        print(f"{self.name} speeds past at lightning speed!")

    hero1 = Superhero("ShadowBlade", "Invisibility", "New York")
    hero2 = FlyingHero("SkyWing", "Flight", "Metropolis", 10000)
    hero3 = SpeedHero("FlashNova", "Super Speed", "Central City")

    hero1.introduce()
    hero2.introduce()
    hero3.introduce()

    hero1.move()
    hero2.move()
    hero3.move()


##QUESTION 2 
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print(" The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print(" The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print(" The boat is sailing on the water.")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
