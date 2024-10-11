# filter() = creates a collection of elements from an iterable
#              for which a function returns

# filter(function,iterables)

# nums = ['Anil','Ankita','Ashish','Lenka','Biswaprakash']
# func = lambda words: len(words) >= 5
# filter = list(filter(func,nums))
#
# print(filter)

# ------------------------------------------

details = [
    ('Anil',21),
    ('Ankita',34),
    ('Sunil',9),
    ('GUdu',12),
    ('Sayani',23),
    ('Sipra',12),
]

func = lambda age:age[1] >= 18

filter = list(filter(func,details))

# print(filter)

for i in filter:print(i[0]  +':'+ str(i[1]))

