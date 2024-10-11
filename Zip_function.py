# zip(iterables) = aggregate elements fro m two or more iterables
#                  (list,tuples,sets,etc.)
#                  creates a zip object with paired elements stored in
#                  tuples for each element.

username = ['Anil','Ankita','Ashish']
password = ('qioeppe','eiowp','2910jdjks')
log_in_date = ['1/12/2023,','23/12/2023','14/3/2024']


usern_useP = list(zip(username,password,log_in_date))

for i in usern_useP:
    print(i)

