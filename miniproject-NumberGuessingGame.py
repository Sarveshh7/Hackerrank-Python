#This is a simple number guessing game
import random
number_to_guess=random.randint(1,100)
while True:
 try:
    guess=int(input("Enter a number b/w 1 to 100:"))
    
    if guess>number_to_guess:
      print("Too high")
    elif guess<number_to_guess:
      print("Too Low")    
    else:
      print("Congrats! You Guessed the number Correctly!")
      break
 except ValueError:
   print("Enter Valid Number!!")
