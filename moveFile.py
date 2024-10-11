import os

source = "copy.txt"

destination = "C:\\mupersonal_details\\scholarship\\copy.txt"

try:
    if os.path.exists(destination):
        print('there is already a file there.')
    else:
        os.replace(source,destination)
        print(source + "Was moved")

except FileExistsError:
          print(source + "was not found")
