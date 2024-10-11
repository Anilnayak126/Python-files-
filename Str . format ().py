# str .format() = optional method that  gives users
#                 more  control when displaying output.

# name = 'Anil'
# age =21

# print("my  name  is {} and i am {} years old".format(name,age))
# print("my  name  is {} and i am {} years old")
# print("my  name  is {1} and i am {0} years old".format(name,age)) #positional arguments
# print("my  name  is {name} and i am {age} years old".format(name = "Sunil",age = 35)) #keyword aguments
# -------------------
# text = 'hello my name is {} and i  am {} years old .'
# print(text.format(name,age))

# -----------------
# left rigth padding by through format
# name = "Anil"
# print('Hello  my name is {}, nice to meet uh'.format(name))
# print('Hello  my name is {:10}, nice to meet uh'.format(name))
# print('Hello  my name is {:<10}, nice to meet uh'.format(name))
# print('Hello  my name is {:>10}, nice to meet uh'.format(name))
# print('Hello  my name is {:^10}, nice to meet uh'.format(name))
# -----------------------
# to rmv floating  point  number
# number = 3.14159
number = 1000
print('the number pi is {:.3f}'.format(number))
print('the number is {:,}'.format(number))
print('the number is {:b}'.format(number)) #binary
print('the number is {:o}'.format(number))
print('the number is {:X}'.format(number)) #hexdecimal
print('the number is {:E}'.format(number)) #scientific notetion


