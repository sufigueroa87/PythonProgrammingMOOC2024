# Please write a program which asks the user for a string. The program then prints out the input string in reversed
# order, from end to beginning. Each character should be on a separate line.
#
# An example of expected behaviour:
#
# Please type in a string: hiya
# a
# y
# i
# h

string = input("Please type in a string: ")

count = len(string) - 1

while count >= 0:
    print(string[count])
    count = count - 1