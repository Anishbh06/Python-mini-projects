import random

max_number = input("Enter the range of numbers from which you want to guess \n")

if max_number.isdigit():
    max_number = int(max_number)
else:
    print("Invalid")
    quit()

random_number = random.randrange(0,max_number)

no_guess = 0
while True:
    no_guess += 1
    answer = input("Enter your guess")

    if answer.isdigit():
        answer = int(answer)
    else:
        print("Incalid input")
        continue
    
    if answer == random_number:
        print("You got it")
        break
    else:
        print("You did not get it loser")

print(f"You got it in {no_guess} guesses")