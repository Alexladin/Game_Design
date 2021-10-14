#Word Game
# Alex Ladin
#09/29/2021
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word

import random, os

os.system('cls')
#function to update dashes and letters
def updateWord(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print('_', end=' ')
def Menu() :
    print("##############################################")
    print("Select the number which you would like to play")
    print("#                  MENU                      #")
    print("#                                            #")
    print("#      1. Animals                            #")
    print("#      2. Computer Parts                     #")
    print("#      3. Fruits                             #")
    print("#      4. Exit                               #")
    print("# To play the game select 1-3 to exit select 4")
    print("##############################################")
#allows the user to type and makes sure the code doesnt break and they dont put an integer
    while 1:
        sel=input("What would you like to do? ")
        try:
            sel = int(sel)
            break
        except ValueError:
            print("This is not an integer")
    
    return sel
#this is a funcion for playing the level the user chooses
def selWord(sel) :
    if sel ==1 : 
        word= random.choice(animals)
    elif sel==2:
        word=random.choice(compParts)
    else:
        word=random.choice(fruit)
    return word
#this is the list that could be guessed on each level 
animals=["tiger", "elephant", "dog", "cat", "bear", "zebra"]
fruit=["banana", "strawberries","watermelon", "grapes","rasberries", "pineapple"]
compParts=["keyboard", "Monitors", "computer","trackpad", "case","Operating System"]
name= input("What is your name? ")
maxscore=0 #to score highest score 
counter=0
sel=Menu()
print(sel)
while sel <=3 :
#this gives the user instructions and keeps track of their turns to make sure they dont have unlimited tries 
    print(name, " Good Luck! you have 5 chances to guess")
    turns=1
    counter +=1
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    letCount=0
    print(word) # just for checking our code delete later
    guesses=''
    updateWord(word, guesses)
#funcion for getting the users name and having them put in a letter also keeping track of letters in the word
    while turns > 0 and letCount< wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess
            letCount +=1
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        updateWord(word, guesses)
        #funcion for calculating the users score 
    score=3*wordCount+5*turns
    # os.system('cls')
    if score > maxscore:
        maxscore=score
    print(maxscore)
    
    sel=Menu()
#funcion for keeping the users name in score in a diffrent file which saves 

anotherFile = open("score.txt", "a")
anotherFile.write("\n" + name +"  highest score: \t" + str(maxscore))
anotherFile.close()