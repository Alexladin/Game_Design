#alexladin
#arithmetic operators 
# + - * / %
# check for even numbers

import os
os.system('cls')

num=int(input("give me a number"))
rem=num
#conditoinal
if(rem==num):
    print(rem%10)
else:
    print("fail")
    num=int(input("give me a number"))
rem=num
#conditoinal
if(rem==num):
    print(rem%100)
else:
    print("fail")
    num=int(input("give me a number"))
rem=num
#conditoinal
if(rem==num):
    print(rem%1000)
else:
    print("fail")