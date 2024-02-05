# In the Python math module there is the function sqrt, which calculates the square root of a number. You can use it
# like so:
#
# from math import sqrt
#
# print(sqrt(9))
#
# This should print out
# Sample output
#
# 3.0
#
# We will return to the concept of a module and the import statement later. For now, it is sufficient to understand that
# the line from math import sqrt allows us to use the sqrt function in our program.
#
# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c.
# It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt
# function is as follows:
#
# x = (-b ± sqrt(b²-4ac))/(2a).
#
# You can assume the equation will always have two real roots, so the above formula will always work.
#
# An example of expected behaviour:
# Sample output
#
# Value of a: 1
# Value of b: 2
# Value of c: -8
# 
# The roots are 2.0 and -4.0

from math import sqrt

valueA = int(input("Value of a: "))
valueB = int(input("Value of b: "))
valueC = int(input("Value of c: "))

floatRaiz = sqrt(valueB ** 2 - (4*valueA*valueC))

result1 = ((-1*valueB) + floatRaiz) / (2*valueA)

result2 = ((-1*valueB) - floatRaiz) / (2*valueA)

print(f"The roots are {result1} and {result2}")