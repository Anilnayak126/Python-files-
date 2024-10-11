# scope = the region that a  variable is reconized
#        A variable is  only availble from inside the  region it is created .
#        A global and locally scoped  version  of a varibale can be created.


# L,E,G,B = local,Enclosing,global,Built-in



name = "Anil"

def displayname():
    name = "sunil"
    print(name)


displayname()
print(name)