# Dictionary Comprehension =  create dictionaries using an expression can replace for loops
#                                and certain lambda fucntion


# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional }
# dictionary = {key: (if/else) for (key,value) in iterable }
# dictionary = {key: function(value) for (key,value) in iterable }

# cities_temperture = {'Bhubaneswar':34,'Bhadrak':36,'Cuttack':30,'Anugul':23}
# print(cities_temperture)
# print('-' * 50)
# cities_temperture_in_F = {key: round((value -32) * (5/9)) for (key,value) in cities_temperture.items()}
# print(cities_temperture_in_F)
# print('-' * 50)

# -----------------------------------------------------------------
# weather = {'Bhubaneswar':'cloudy','Bhadrak':'snowing','Cuttack':'rain','Anugul':'cloudy'}
#
# rainy_cities = {key: value for key,value in weather.items() if value == 'rain'}
# cloudy_cities = {key: value for key,value in weather.items() if value == 'cloudy'}
# snowing_cities = {key:value for key,value in weather.items() if value == 'snowing'}
#
#
# print(snowing_cities)
# print(cloudy_cities)
# print(rainy_cities)
# ---------------------------------------------------------
# cities_temp = {'Bhubaneswar':34,'Bhadrak':24,'Cuttack':45,'Anugul':40}
#
# Helthy_weather = {key: ('Good'if value <= 30  else 'bad' ) for (key,value) in cities_temp.items()}
# print(Helthy_weather)
#
# warm_cold = {key:('cold' if value <= 30 else 'warm') for (key,value) in cities_temp.items()}
# print(warm_cold)
# ------------------------------------------------
cities_temp = {'Bhubaneswar':34,'Bhadrak':24,'Cuttack':45,'Anugul':40}



def add(temp):
    if temp >= 30:
        temp = temp - 5
    else:
        temp += 2
    return  temp

add_temp = {key: add(value) for (key,value) in cities_temp.items()}


print(add_temp)
print(cities_temp)










