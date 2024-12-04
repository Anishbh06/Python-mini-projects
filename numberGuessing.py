import random
import os
clear = lambda: os.system('cls')
clear()

random_number = random.randint(0,100)
print(random_number)
win = False

def gameplay(attempts):
   global win
   while win != True:
    print(f"You have {attempts} attempts left.")
    guess = int(input("\nEnter your guess: "))   
    if attempts == 1:
         print(f"You ran out of attempts. The number was {random_number}")
         quit()
    elif guess > random_number:
         attempts -= 1
         print("\nToo high")
         continue
    elif guess < random_number:
         attempts -= 1
         print("\nToo low")
         continue
    else:
         win = True
def start():  
 level = int(input("I have picked a number. Pick A difficulty level\n 1:Easy\n 2:Hard\n"))
 if level == 1:
   attempts = 10
   gameplay(attempts)
 else: 
   attempts = 5
   gameplay(attempts)

start()
print("\n CONGRATULATIONS YOU GUESSED THE CORRECT NUMBER")
