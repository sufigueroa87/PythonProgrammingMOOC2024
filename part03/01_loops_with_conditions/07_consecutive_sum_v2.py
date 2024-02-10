# Please write a new version of the program in the previous exercise. In addition to the result it should also print
# out the calculation performed:
#
# Limit: 2
# The consecutive sum: 1 + 2 = 3
#
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10
#
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21
#
# You may assume the number typed in by the user is always equal to 2 or higher.

limit = int(input("Limit: "))

number = 1

suma = 0

printSum = "The consecutive sum:"

while suma < limit:

    suma = suma + number

    if suma < limit:
        printSum = f"{printSum} {number} +"
    else:
        printSum = f"{printSum} {number}"

    number = number + 1

print(f"{printSum} = {suma}")