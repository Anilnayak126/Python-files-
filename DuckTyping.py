# Duck typing = concept where the class of an object is less important than the methods
#               class type is not checked if minimum methods/attributes are present
#               "If it was like a duck, and it quacks like a duck", then it must be a duck.


class duck:
    def walk(self):
        print('it walk  like a duck')
    def talk(self):
        print('its talk like duck.')

class chicken:
    def walk(self):
        print('its walk  like a chicken.')
    def talk(self):
        print('its talk like a chicken')

class person:
    def catch(self,duck):
        duck.walk()
        duck.talk()



duck1 = duck()
chicken1 = chicken()
person1 = person()

person1.catch(chicken1)