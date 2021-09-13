#Alex Ladin
#9/13/21
#This is about data type
#how strings work 
import os
os.system ('cls')
userInput=input ("type something")
print (type(userInput))
try:
    int(userInput)
    check=True
except ValueError:
    check=False

if (check):
    #I will be back
    print()
else:
    print(len(userInput))
for i in userInput :
    print(i)
if len(userInput>3):
    print (userInput[3])
