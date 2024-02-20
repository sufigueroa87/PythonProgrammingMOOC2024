# Please write a program which asks the user to type in a sentence. The program then prints out the first letter
# of each word in the sentence, each letter on a separate line.
#
# An example of expected behaviour:
#
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

import re

sentence = input("Please type in a sentence: ")

match = True

print(sentence[0])

while match:
    resultado = re.search(' ', sentence)
    if resultado:
        posicionPrimeraLetra = resultado.span()[1]
        print(sentence[posicionPrimeraLetra])
        sentence = sentence[posicionPrimeraLetra:len(sentence)]
    else:
        match = False
