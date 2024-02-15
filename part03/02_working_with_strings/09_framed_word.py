# Please write a program which asks the user for a string and then prints out a frame of * characters with the word
# in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit
# inside the frame.
#
# If the length of the input string is an odd number, you may print out the word in either of the two possible centre
# locations.
#
# Word: testing
#
# ******************************
# *          testing           *
# ******************************

word = input("Word: ")

cantidad_espacios_en_blanco = int((30 - 2 - len(word)) / 2)

espacios_blanco = cantidad_espacios_en_blanco * " "

print("*"*30)

if len(word) % 2 == 0:
    print(f"*{espacios_blanco}{word}{espacios_blanco}*")
else:
    print(f"*{espacios_blanco}{word}{espacios_blanco} *")

print("*"*30)