# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
# The program should then print out the number of times the user tried different codes.
#
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts

correctPin = False

valuePinCorrect = "4321"

count = 0

while not correctPin:
    valuePinUser = input("PIN: ")
    count = count + 1
    if valuePinUser != valuePinCorrect:
        print("Wrong")
    else:
        correctPin = True

if count == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {count} attempts")