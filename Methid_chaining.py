# method chaining = calling multiple methods sequetially each call
#                  perform an action on the same object and returns self.

class Car:
    def drive(self):
        print("You drive the car !")
        return  self

    def turnoff(self):
        print("You  turn off the  car !")
        return  self
    def brake(self):
        print("You step on  the breaks !")
        return  self


car1 = Car()

car1.drive().\
     brake().\
     turnoff()

