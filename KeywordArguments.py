# keyword Arguments = arguments preceded by  an identifier when we pass them to a function
#                     the order of the arguments doesnt matter, unlike positional arguments
#                    python known the names of the arguments that our function receives

def hello(fname,middlename,lname):
    print(f"hello {fname} {middlename} {lname}")

hello(fname="Anil",lname='nayak',middlename='kumar')
