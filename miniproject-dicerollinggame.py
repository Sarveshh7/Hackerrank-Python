#This is a basic dice rolling game 
import random

while True:
    s=input("Roll a dice (y/n):")
    if(s.lower()=='y'):
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'{die1},{die2}')
        
    elif(s.lower()=='n'):
        print("Thanks for Playing!")
        break
    else:
        print("enter a valid choice!")
        break
