# sort() method = used with lists
# sort function = used with iterables

# student = ["Anil","Sunil","Priyanka","Anita"]

#
# student.sort(reverse=True)
#
# for i in student:
#     print(i)
# ----------------------------------------Sorted a tuple

# student = ("Anil","Sunil","Priyanka","Anita")
#
# sorted_student = sorted(student,reverse=True)
#
# for i in sorted_student:
#     print(i)

student = [("Anil","F",23),
            ("Sunil","A",21),
            ("Ankita",'B',20),
            ("Ayush","C",29)]


# -----------------------------for list
grade = lambda grades:grades[1]
age = lambda age:age[2]
student.sort(key = age,reverse=True)
print(student)
# -----------------------------for  tuples
students = (("Anil","F",23),
            ("Sunil","A",21),
            ("Ankita",'B',20),
            ("Ayush","C",29))

grade = lambda grades : grades[1]
sorted = sorted(students,key= grade,reverse=True)

for i in sorted:
    print(i)
