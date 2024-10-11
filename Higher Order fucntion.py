# Higher Order Function = a function that either:
#                         1.accepts a function as an arguments
#                         or
#                         2. returns a function
#                         (In python , Function are also  treated as a object)

# def loud(text):
#     return  text.upper()
#
# def quit(text):
#     return  text.lower()
#
#
# def Hello(func):
#     text = func("HELLO")
#     print(text)
#
#
# Hello(quit)

#-------------------------------------- Example -2

def divisor(x):
    def dividend(y):
        return  y / x
    return  dividend

divide = divisor(2)
print(divide(12))
