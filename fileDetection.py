import os

path = "C:\\Users\\nayak\\OneDrive\\Pictures\\Screenshots\\Screenshot 2024-04-21 172934.png"

if os.path.exists(path):
    print("that loaction exist")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("this is directory")
else:
    print("that location does n't exist")