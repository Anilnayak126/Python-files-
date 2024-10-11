# logical operators (and,or,not)= used to check if two or  more conditional

temp = int(input("what bis the temperture outside:"))

if not(temp >= 0 and temp <= 30):
    print("temp is bad today")
    print('saty inside')
elif not( temp < 0 or temp > 30):
    print('the temperture is good today')
    print('go  oustside')
