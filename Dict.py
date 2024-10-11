# dictionary = A changeable, unOrdered collections of unique key:value pairs
#             fast because they use hashing, allow us to access a value quickly

# capitals = {
#     "USA":'washington DC',
#     "INDIA":'newdelhi',
#     'Russia':'bejings'
# }
#
# capitals.update({'Geramny':"Berlin"})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('USA')
# # capitals.clear()

# print(capitals['Russia'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals)
#
# for key,value in capitals.items():
#     print(key ,value,end=',')


# nested Dict


test_dict = {'GFG': {'rate': 4, 'since': 2012}}
test_dict['GFG']['rank'] = 1

rate = test_dict['GFG']
print(rate)
print(test_dict)