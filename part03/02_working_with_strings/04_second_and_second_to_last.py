# Please write a program which asks the user for a string. The program then prints out a message based on whether
# the second character and the second to last character are the same or not. See the examples below.
#
# Please type in a string: python
# The second and the second to last characters are different
#
# Please type in a string: pascal
# The second and the second to last characters are a

string = input("Please type in a string: ")

second = string[1]

second_to_last = string[len(string)-2]

if second != second_to_last:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {second}")