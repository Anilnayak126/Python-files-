# **kwargs = parameter that will pack  all arguments into  a dictionary
#  useful so that a fucntion can accept a  varying amount of keyword argument.

def hello(**kwargs):
    # print(f"Hello {kwargs['titel']} {kwargs['first']} {kwargs['last']}")
   # print('Hello',end=" ")
   #
   for key,value in kwargs.items():
       print(value,end=" ")



hello(titel ="Mr.",first="Anil",middle = "kumar",last='nayak')

