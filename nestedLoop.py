# nestedLoops = the "inner loop" will  finish all of its iterationas
#              before finishing one iteration of the "Outerloop".


rows = int(input("Enter ur rows:"))
columns = int(input("How many columns:"))
symbol = input("Enter a symbol to use :")

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()
