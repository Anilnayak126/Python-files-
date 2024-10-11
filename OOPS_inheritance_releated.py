class person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def details(self):
        print(f"hello my name is {self.fname +' '+ self.lname} and i am {self.age} years old.")


psn = person("Anil","nayak",22)

psn.details()