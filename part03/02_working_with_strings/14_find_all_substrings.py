# Please make an extended version of the previous program, which prints out all the substrings which are at least
# three characters long, and which begin with the character specified by the user. You may assume the input string
# is at least three characters long.
#
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot
#
# Please type in a word: banana
# Please type in a character: n
# nan

string = input("Please type in a word: ")
caracter = input("Please type in a character: ")

encontrado = True

while encontrado:
    if string.find(caracter) >= 0:
        posicion = string.find(caracter)
        resultado = string[posicion:posicion+3]

        if len(resultado) == 3:
            print(resultado)

        string = string[posicion+1:len(string)]
    else:
        encontrado = False

