#AlexLadin
#9-15-21
#random number between 1 and 100 inclusive 
#give the user 10 chances to guess 
#when the user guess plus one chances then check if guess is above or below anwser
# if parenthesus random number minus guess is greater than 25, too high

import random, os
number = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50: "))

while guess != number:
    if guess < number:
        print ("You need to guess higher. Try again")
        guess = int(input("\nGuess a number between 1 and 50: "))
    else:
        print("You need to guess lower. Try again")
        guess = int(input("\nGuess a number between 1 and 50: "))

print("You guessed the number correctly!")

