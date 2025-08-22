#This program is built to identify the number and type of each character in a word. Like, BOOK has 1 B, 2 O, 1 K.

word = input("Please type a word, entirely in capital letters: ")
array = []
for x in word:
    array.append(x)
newarray = []
for y in array:
    if y not in newarray:  
        newarray.append(y)
variables = dict.fromkeys(newarray)

for checker in newarray:
    variables[checker] = 0
print(variables)


checker1 = 0
checker2 = 0
while checker1 >=0 and checker1 < len(array):
    storagea = array[checker1]
    checker2 = 0
    while checker2 >= 0 and checker2 < len(newarray):
        storagena = newarray[checker2]
        if storagea == storagena:
            variables[storagena] += 1
        checker2 += 1
    checker1 += 1

print(variables)


