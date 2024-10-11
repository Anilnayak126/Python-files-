# map() = applies a function to  each items in an iterable (list,tuple,etc)
# map(function,iterables)


# store = [12,34,4,556,657,7,6,7]
# func = lambda x:x+2
# add = list(map(func,store))
# print(add)


# ----------------------
# store = [12,344,5656,7687,877]
# func = lambda x:x % 2 == 0
# filter = list(filter(func,store))
# print(filter)
# ----------------------------

store = [
    ('Shirt',234),
    ('Pant',237),
    ('T-shirt',2345),
    ('half-Pant',755),
         ]

to_euros = lambda data: (data[0],data[1] * 0.82)
to_dollar = lambda data : (data[0],data[1] /0.82)


store_price = list(map(to_euros,store))
new_store_p = list(map(to_dollar,store))

for i in store_price:print(i)
print('--------------------------------------')
for i in new_store_p:print(i)



