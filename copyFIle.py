# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destricction can be a directory
# copy2() = copy() + copies metadata (file's creation and modificsation)


import shutil

shutil.copyfile('test.txt','copy.txt') #src ,destination