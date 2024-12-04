import random

print("WELCOME TO PLAY ROCK PAPER AND SCISSORS")
quit_game = False;

options = ["r", "p", "s"]

#points
user_points = 0
computer_points = 0

while quit_game != True:
    user_input = input("Enter R: Rock, P: Paper or S: Scissors. Or 'Q' to quit:  ")

    if user_input == "q":
        break
    elif user_input not in options:
        print("Invalid input. Try again.")
        continue
    
    computer_choice = random.choice(options)
    print(computer_choice)


    if user_input == computer_choice:
            print("TIE. \nTry Again")
            
    elif (user_input == ["r"] and computer_choice == ["s"]) or \
            (user_input == ["p"] and computer_choice == ["r"]) or \
            (user_input == ["s"] and computer_choice == ["p"]):
            
            user_points += 1
            print("User wins this round")
    else:
            computer_points +=1
            print("computer wins this round")


print("GAME ENDED")
print(f"The final score of you is {user_points} and the final score of compiter is {computer_points} ")

print("User WINS!!") if (user_points > computer_points) else print("Computer WINS!")
   

