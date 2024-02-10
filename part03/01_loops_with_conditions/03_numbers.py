# Please write a program which asks the user for a number. The program then prints out all integer numbers
# greater than zero but smaller than the input.
#
# Upper limit: 5
# 1
# 2
# 3
# 4

numberLimit = int(input("Upper limit: "))

number = 1

while number < numberLimit:
    print(number)
    number = number + 1