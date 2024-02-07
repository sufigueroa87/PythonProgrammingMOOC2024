# The following program contains several syntactic errors. Please fix the program so that the syntax is in order and
# the program works as specified by the examples below.
#
#   number = input("Please type in a number: ")
#   if number>100
#     print("The number was greater than one hundred")
#     number - 100
#     print("Now its value has decreased by one hundred)
#      print("Its value is now"+ number)
#  print(number + " must be my lucky number!")
#  print("Have a nice day!)

number = int(input("Please type in a number: "))

if number > 100 :
    print("The number was greater than one hundred")

    number = number - 100

    print("Now its value has decreased by one hundred")

    print("Its value is now", number)

print(number, " must be my lucky number!")

print("Have a nice day!")