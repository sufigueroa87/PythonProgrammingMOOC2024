# PRE-TASK
# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until
# the user types in zero.
#
# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

"""
number = -1

while number != 0:
    number = int(input("Number: "))
"""

# PART 1: COUNT
# After reading in the numbers the program should print out how many numbers were typed in. The zero at the end
# should not be included in the count.
#
# You will need a new variable here to keep track of the numbers typed in.
#
# ... the program asks for numbers
# Numbers typed in 4

"""
count = -1

number = -1

while number != 0:
    number = int(input("Number: "))
    count = count + 1

print(f"Numbers typed in {count}")
"""

# PART 2: SUM
#
# The program should also print out the sum of all the numbers typed in. The zero at the end should not be included
# in the calculation.
#
# The program should now print out the following:
#
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34

"""
count = -1

number = -1

sum = 0

while number != 0:
    number = int(input("Number: "))
    count = count + 1
    sum = sum + number

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
"""

# PART 3: MEAN
#
# The program should also print out the mean of the numbers. The zero at the end should not be included in
# the calculation. You may assume the user will always type in at least one valid non-zero number.
#
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5

"""
count = -1
number = -1
suma = 0
mean = 0.0

while number != 0:
    number = int(input("Number: "))
    count = count + 1
    suma = suma + number

mean = suma / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {suma}")
print(f"The mean of the numbers is {mean}")
"""

# PART 4: POSITIVES AND NEGATIVES
#
# The program should also print out statistics on how many of the numbers were positive and how many were negative.
# The zero at the end should not be included in the calculation.
#
# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1

count = -1
number = -1
suma = 0
mean = 0.0
countPositiveNumbers = 0
countNegativeNumbers = 0

print("Please type in integer numbers. Type in 0 to finish.")

while number != 0:
    number = int(input("Number: "))

    if number > 0:
        countPositiveNumbers = countPositiveNumbers + 1

    if number < 0:
        countNegativeNumbers = countNegativeNumbers + 1

    count = count + 1
    suma = suma + number

mean = suma / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {suma}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {countPositiveNumbers}")
print(f"Negative numbers {countNegativeNumbers}")