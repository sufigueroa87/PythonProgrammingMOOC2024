# Please write a program which finds the second occurrence of a substring. If there is no second (or first)
# occurrence, the program should print out a message accordingly.
#
# In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the
# substring aa is at index 2.
#
# Some examples of expected behaviour:
#
# Please type in a string: abcabc
# Please type in a substring: ab
# The second occurrence of the substring is at index 3.
#
# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.
#
# Please type in a string: aybabtu
# Please type in a substring: ba
# The substring does not occur twice in the string.

# Encontrar la posición del segundo match

import re

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

count = 0

for match in re.finditer(substring, string):
    count = count + 1
    if count == 2:
        print(f"The second occurrence of the substring is at index {match.start()}.")

if count < 2:
    print("The substring does not occur twice in the string.")