class Car:
    color = None

class motorcycle:
    color = None

def changeColor(car,color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

bike1 = motorcycle()
bike2 = motorcycle()
bike3 = motorcycle()

changeColor(bike3,color="blue")
changeColor(bike2,color="yellow")
changeColor(bike1,color="Green")

changeColor(car2,color="red")
changeColor(car1,color= "blue")
changeColor(car3,color= "green")

print(car3.color)
print(car2.color)
print(car1.color)
print("---------------------------------------------")
print(bike1.color)
print(bike2.color)
print(bike3.color)

