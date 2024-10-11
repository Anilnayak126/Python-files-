# exception = events detected during execution that interrupt the flow of a program
try:
   numerator = int(input("Enter a  number to  divide:"))
   denominator = int(input("Enter number to  divided:"))
   result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print('u  cant divided by zero')
except ValueError as e:
    print(e)
    print("u  can't divided by a string")
except Exception as e:
    print(e)
    print("some thing went wrong")
else:
    print(result)
finally:
    print('this will always execute')


