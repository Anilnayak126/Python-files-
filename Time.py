import time

# print(time.ctime(0)) #convert a time expressed since epoch to  a readble string
                    # epoch = when ur computer thinks time began (reference point)
# print(time.time()) # return current second  since  path

# time_object = time.localtime()
# print(time_object)
# localime = time.strftime(
#     '%B /%d/ %y, %H-%M-%S',time_object
# )
# print(localime)

# -----strp
# time_string = '20 April, 2020'
# time_object = time.strptime(time_string,'%d %B, %Y')
# print(time_object)

#(year, month, day, hours, minutes, secs , # day of the week, #day of the year )
time_tuple = (2020,4,20,4,20,0,0,0,0)
# time_string = time.asctime(time_tuple)
time_string = time.mktime(time_tuple)
print(time_string)

