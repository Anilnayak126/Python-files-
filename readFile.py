try:
   with open('test.txt') as file:
      print(file.read())
except FileExistsError:
    print("that file was not  found")

# print(file.closed)