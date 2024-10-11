# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#             performs function on first two elements and repeats process untill i value remains

# reduce(function,iterables)

import functools

# letters = ['A','N','I','L']
# func = lambda  x,y:x+y
# word = functools.reduce(func,letters)
# print(word)

nums = [12,34456,576,76,87,9,798]
sum = functools.reduce(lambda x,y : x+y,nums)
print(sum)

factorial = functools.reduce(lambda x,y:x*y,nums)
print(f'factorila : {factorial}')
