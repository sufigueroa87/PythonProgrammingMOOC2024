# Please write a program which asks for the names and ages of two persons. The program should then print
# out the name of the elder.
#
# Some examples of expected behaviour:
#
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada

print("Person 1: ")
namePerson1 = input("Name person1: ")
agePerson1 = int(input("Age person1: "))

print("Person 2: ")
namePerson2 = input("Name person2: ")
agePerson2 = int(input("Age person2: "))

if agePerson1 > agePerson2:
    print(f"The elder is {namePerson1}")
elif agePerson2 > agePerson1:
    print(f"The elder is {namePerson2}")
else:
    print(f"{namePerson1} and {namePerson2} are the same age")
