# list = used to store multiple items in a single variable

food = ['pizza', 'humburger', 'hotdog']
num = [1,34,5,67,8,]
food[0] = 'sushi'

# food.append('icecream')
# food.remove('hotdog')
# food.pop()
# food.insert(3,'Cake')
# num.sort()
# food.clear()
print(food)

#
# for i in food:
#     print(i[::-1],end='+')


Number = ["a",'b',2,'c',3]
str = [item for item in Number if type(item) == str]
int = [item for item in Number if type(item) == int]
print(f"Number : {str}" )
print(f"List : {int}")


