stars= int(input(" Enter number of stars: "))
line= stars
space= 0

for i in range (line):
    for counter in range(stars):
        print("* ", end=" ")
    

    for j in range(space):
        print ("  ", end=" ")
    space+= 2

    for counter in range (stars):
        print ("* ", end= " ")

    print( )
    stars-= 1


print ("thank you")

