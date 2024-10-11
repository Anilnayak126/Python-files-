# nested function calls = functions calls inside other function calls
#                         inner most function calls are resolved first
#                         returned value is used as  argument for the next
#                        outer function.
# import math
#
# num = input('nter a whole positive number:')
# num = float(num)
# num = abs(num)
# num = math.ceil(num)
# print(num)

# shortHAnd
print(round(abs(float (input('nter a whole positive number:')))))

