# list comprehension = a way to create new list with less syntax
#                      can mimic certain lambda functions, easier to read .
#                        list = [expression for item in iterble]
#                        list = [expression for item in iterble if conditional]
#                        list = [expression if/else for item in iterble]


# even =sum([even for even in range(0,20,2)])
#
# print(even)
# ]-----------------------------
# squares = [sq * sq for sq in range(1,11)]
#
# print(squares)

# ----------------------------------
# result = [12,34,45,67,78,67,45,34]
# pass_rate = list(filter(lambda x:x >= 30,result))
# print(f'Pass :{pass_rate}')
# fail_rate = list(filter(lambda x:x<= 30,result))
# print(f'Fail : {fail_rate}')
# -----------------------------------------

result = [12,34,45,67,78,67,45,34]
pass_res = [res for res in result if res >= 30]
print(pass_res)
fail_res = [res for res in result if res <= 30]
print(fail_res)


# ------------------------------
fail = [res if res >= 30 else 'failed' for res in result]
print(fail)




