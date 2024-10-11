# lambda function = function written in 1 line using lambda keyword
#                  accepts any number of  arguments, but only has one expression
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time , throw-away)

# lambda parameter:expression


double = lambda x:x * 2
say = print
say(double(10))

fullname =  lambda fname,lname: f"{fname} {lname}"
say(fullname("Anil","Nayak"))

multiply = lambda x,y: x * y
say(f"the multiply of  ur number : {multiply(12,12)}" )

add = lambda x,y,z: x + y + z
say(f"the total value :{add(1,34,5)}")

age = lambda age:  print("allowed") if age >= 18 else say("Not eligible")

age(18)


