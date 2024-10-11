# multi level inheritance = when  a derived (child) class inherit  another derived (child) class

class Oragenism:
    Alive = True
class Animal(Oragenism):
    def eat(self):
        print("This animal can eat")
class Dog(Animal):
    def bark(self):
        print("This animal can bark.")

dog = Dog()
print(dog.Alive)
dog.eat()
dog.bark()

