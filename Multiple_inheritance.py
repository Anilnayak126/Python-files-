# mulitple inheritance = when a child class is derived from more than one parent class

class Prey:
    Alive = True
    def flees(self):
        print("this animal flees")


class Predator:
    Alive = True
    def hunt(self):
        print("this animal is hunting ")

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

class Hawk(Predator):
    pass


hawk = Hawk()
fish = Fish()
rabbit = Rabbit()

hawk.hunt()
fish.hunt()
fish.flees()

