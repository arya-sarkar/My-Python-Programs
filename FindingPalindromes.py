# This is a program to identify whether a word is a palindrome. 

word = input("Please type a word, entirely in capital letters: ")
array = []
for x in word:
    array.append(x)
length = len(array) - 1
newarray = []
while length != -1:
    newarray.append(array[length])
    length -= 1
counter = 0
checker = 0
while checker >= 0 and checker < len(array):
    valA = array[checker]
    valB = newarray[checker]
    if valA == valB:
        counter +=1
    checker += 1
if counter == len(array):
    print("The word is a palindrome.")
else:
    print("Not a palindrome.")




