# Write a program which asks for the user's name and address. The program should also print out the given information,
# as follows:
#
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

name = input("What is your name?")
surname = input("What is your surname?")
address = input("What is your address?")
cityAndPostalCode = input("What is your city and your postal code?")

print(name + " " + surname)
print(address)
print(cityAndPostalCode)

