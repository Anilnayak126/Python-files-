import os
import shutil
path = 'empty_file'


try:
    # os.remove(path)#for remove filepath
    # os.rmdir(path) # for remove directory
     shutil.rmtree(path) # to  delete all file inside a directory
except FileNotFoundError:
    print("the file  is not found")
except PermissionError:
    print('u dont have permision to delet that ')
except OSError:
    print("You Can't delete  that using that  function.")
else:
    print(path+ "was deleted")