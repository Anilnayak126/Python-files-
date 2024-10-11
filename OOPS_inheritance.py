class Animal:
   Alive = True
   def eat(self):
       print("this animal can eat")
   def sleep(self):
       print("This animal can  Sleep")

class Rabbit(Animal):
   def run(self):
       print("this  rabbit can  swim")
class Fish(Animal):
    def swim(self):
        print('This animal is sleeping')
class Hawk(Animal):
    def fly(self):
        print("this animal  can fly")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.Alive)
hawk.eat()
fish.sleep()
hawk.fly()
