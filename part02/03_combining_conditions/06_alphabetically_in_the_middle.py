# Please write a program which asks the user for three letters. The program should then print out whichever
# of the three letters would be in the middle if the letters were in alphabetical order.
#
# You may assume the letters will be either all uppercase, or all lowercase.
#
# Some examples of expected behaviour:
#
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

letters = letter1 + letter2 + letter3

sorted_letters = sorted(letters)

print(f"The letter in the middle is {sorted_letters[1]}")