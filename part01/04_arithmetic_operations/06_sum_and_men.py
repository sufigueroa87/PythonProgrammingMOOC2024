# Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.
#
# The program should function as follows:
# Number 1: 2
# Number 2: 1
# Number 3: 6
# Number 4: 7
# The sum of the numbers is 16 and the mean is 4.0

number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
number3 = int(input("Enter the number3: "))
number4 = int(input("Enter the number4: "))
suma = number1 + number2 + number3 + number4
print(f"The sum of the numbers is {suma} and the mean is {suma / 4}")