# Please write a program which prints out all the even numbers between two and thirty, using a loop. Print
# each number on a separate line.
#
# The beginning of your output should look like this:
#
# 2
# 4
# 6
# 8
# etc...

number = 2

while 2 <= number <= 30:

    if number % 2 == 0:
        print(number)

    number = number + 1