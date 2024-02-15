# Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash
# characters accordingly.

width = int(input("Width: "))
height = int(input("Height: "))

count = 0
while count < height:
    print("#"*width)
    count = count + 1