# super() = function used to give access to  the methods of a parent class.
#            Returns  a temporary object of a parent class when used


class Rectangular:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def About(self):
        print("Its all about geometry.")

class Square(Rectangular):
    def __init__(self,length,width):
        super().__init__(length,width)


    def square(self):
        return  self.width * self.length

class Cube(Rectangular):
    def __init__(self,length,height,width):
        super().__init__(length,width)
        self.height = height


    def cube(self):
        return self.height*self.length*self.width


cube = Cube(12,24,56)
square = Square(23,34)

square.About()
print(square.square())

cube.About()
print(cube.cube())




