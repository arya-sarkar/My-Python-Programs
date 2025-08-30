#This program is used to sort numbers taken in a list. (DESCENDING ORDER)

numbers = []
x = 0
while x < 1:
    var1 = int(input("Please type a number."))
    numbers.append(var1)
    var2 = input("DO you want more numbers? If yes, type 'Y'. If no, type 'N'.")
    if var2 == 'Y':
        x = 0
    else:
        x = 1

# ----------------------------------------------------------------------------------------------- #

for a in range(len(numbers)):
    for b in range(len(numbers) - 1):
        itema = numbers[a]
        itemb = numbers[b]
        if itema > itemb:
            numbers[a] = itemb
            numbers[b] = itema

print(numbers)
print("That was in descending order. Dhanyavad, deviyon aur sajjanon.")

