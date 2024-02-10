# Please change the program from the previous exercise so that the user gets to input also the base which is
# multiplied (in the previous program the base was always 2).
#
# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27

upper_limit = int(input("Upper limit: "))

base = int(input("Base: "))

number = 1

while number <= upper_limit:
    print(number)
    number = number * base