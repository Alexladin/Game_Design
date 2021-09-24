import random
Flag=True
answer = input ("Do you want to play a game?")
while 'y' in answer :
    fruits=["apple", "banana", "Berries", "Watermelon" , "pineapple" , "kiwi"]
    MyFruit= random.choices(fruits)
    print(MyFruit)
    counter=5
    while(Flag and counter >0):
        guess= input("guess the fruit ")      
        if guess in MyFruit :
            print ("you won")
            Flag=False     
        else:
            print("you need to guess again")
            counter=counter-1
    
    answer = input("Do you want to play agian?")
if counter==0: 
    print("sorry you lost") 
else:
    print("you won in,", counter)   
print("thank you for playing the game")