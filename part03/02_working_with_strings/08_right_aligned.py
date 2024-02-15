# Please write a program which asks the user for a string and then prints it out so that exactly 20 characters
# are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
#
# You may assume the input string is at most 20 characters long.

string = input("Please type in a string: ")

cantidad_asteriscos = 20 - len(string)

asteriscos = "*"*cantidad_asteriscos

print(f"{asteriscos}{string}")