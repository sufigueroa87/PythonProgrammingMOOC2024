# Please write a program which asks the user for an integer number. The program should then print out the magnitude
# of the number according to the following examples.
# Sample output
#
# Please type in a number: 950
# This number is smaller than 1000
# Thank you!
# Sample output
#
# Please type in a number: 59
# This number is smaller than 1000
# This number is smaller than 100
# Thank you!
# Sample output
#
# Please type in a number: 2
# This number is smaller than 1000
# This number is smaller than 100
# This number is smaller than 10
# Thank you!
# Sample output
#
# Please type in a number: 1123
# Thank you!

numberInteger = int(input("Please type in a number: "))

if 100 < numberInteger < 1000:
    print("This number is smaller than 1000")
elif 10 < numberInteger < 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
elif numberInteger < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")

print("Thank you!")