#Python interpreter sets 'Special variables', one which is __name__.
# Python will assign the __name__ variable a value of '__main__' if its
#the intial module being run.
# --------------------------------------
# if __name__ == '__main__':
# -----------------------------------------
# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

def hello(user_name):
    print(f"hello {user_name} ")


if __name__ == '__main__':
    hello('Anil nayak')