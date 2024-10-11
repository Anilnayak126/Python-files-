

# square = lambda fanme,lname:print(f'hii my name is {fanme} {lname}')
#
#
# square('Anil','nayak')

# a = ('Anil','Sunil','Ankita','Banga','Sipu')
# sorted_student = sorted(a,reverse=True)
# for i in sorted_student:
#     print(i)

students_Detail =(('Anil','M',21),
                   ('Viveka sir','M',21),
                   ('Romya','M',23),
                   ('Ankita','F',56),
                   ('Sunil','M',34)
                   )

# lambda_func = sorted()
# Grade = lambda grade:grade[1]
#
# students_Detail.sort(key=Grade)
#

# age = lambda age:age[2]
# students_sorted = sorted(students_Detail,key=age)
# for i in students_sorted: print(i)

# def upper(s):
#     word = s.split(' ')
#     for i in word:
#        return i[0].upper() + i[1:len(i)],
# s = input(':')
# words  = s.split(' ')
# map = list(map(lambda x:x[0].upper() + x[1:len(x)],words))
# print(' '.join(map))
# def solve(s):
#     upper = []
#
#     words  = s.split(' ')
#     print(words)
#     map = list(map(lambda x:x[0].upper() + x[1:len(x)]),words)
#     return  map
#
#
#
# print(solve(s))

a = 'hello my name is anil kumar nayak'
b = a.split(' ')

def caps(a):
    b = a.split(' ')
    for i in b:
        print(i[0].upper() + i[1:len(i)], end=' ')


caps(a)





