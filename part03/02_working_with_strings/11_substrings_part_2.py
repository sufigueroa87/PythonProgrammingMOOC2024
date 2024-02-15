# Please write a program which asks the user to type in a string. The program then prints out all the substrings
# which end with the last character, from the shortest to the longest. Have a look at the example below.
#
# Please type in a string: test
# t
# st
# est
# test

string = input("Please type in a string: ")

limit = len(string)

count = 0

while count <= len(string):
    print(string[limit-count:limit])
    count = count + 1