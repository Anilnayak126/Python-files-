# Prevents a user from creating an object of that class
# + comples a user to override abstract methods in a child class

# abstract class = A class which contains one or more abstract methods
# abstract method  = a method that has a declaration but does not have an implementation.fr


from abc  import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Bike(Vehicle):
    def go(self):
        print("You ride the bike .")
    def stop(self):
        print("this Bike is stopped")

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print('this car is stopped')


car = Car()
bike = Bike()
# truck = Truck()

car.go()
bike.go()

bike.stop()
car.stop()
