# Please write a program which asks the user to type in a number. The program then prints out all the positive
# integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers
# is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.
#
# Please type in a number: 5
# 2
# 1
# 4
# 3
# 5
#
# Please type in a number: 6
# 2
# 1
# 4
# 3
# 6
# 5

number = int(input("Please type in a number: "))
count = 1

while number > 0 and count <= number:

    if count < number:
        print(count + 1)
    print(count)

    count = count + 2