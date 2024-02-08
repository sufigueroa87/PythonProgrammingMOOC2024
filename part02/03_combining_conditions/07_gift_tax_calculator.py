# Please write a program which calculates the correct amount of tax for a gift from a close relative. Have a look
# at the examples below to see what is expected. Notice the lack of thousands separators in the input values - you
# may assume there will be no spaces or other thousands separators in the numbers in the input, as we haven't yet
# covered dealing with these.
#
# Value of gift: 3500
# No tax!
#
# Value of gift: 5000
# Amount of tax: 100.0 euros
#
# Value of gift: 27500
# Amount of tax: 1950.0 euros

value = int(input("Value of gift: "))

taxExist = False

tax = 0

if value < 5000:
    print("No tax!")
elif 5000 <= value < 25000:
    taxExist = True
    tax = (100 + (value - 5000) * 0.08)
elif 25000 <= value < 55000:
    taxExist = True
    tax = (1700 + (value - 25000) * 0.1)
elif 55000 <= value < 200000:
    taxExist = True
    tax = (4700 + (value - 55000) * 0.12)
elif 200000 <= value < 1000000:
    taxExist = True
    tax = (22100 + (value - 200000) * 0.15)
else:
    taxExist = True
    tax = (142100 + (value - 1000000) * 0.17)

if taxExist:
    print(f"Amount of tax: {tax} euros")