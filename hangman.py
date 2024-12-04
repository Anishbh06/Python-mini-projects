import hangmanlogo as hang
import random
import words 
print(hang.logo)

word_list = words.word_list

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
length = len(chosen_word)

for char in range(length):
    display.append("_")

print(display)

while display.__contains__("_"):
    print(f"\nLives Remaining: {lives}")
    guess = input("Guess a Letter: \n").lower()

    if guess in display:
        print(f"\n{guess} is already Guessed! Guess Another Letter \n")
        continue

    for char in range(len(chosen_word)):
        if chosen_word[char] == guess:
            display[char] = guess
            print(f"Your guess was Correct!\n {guess} is in the word.\n")
        else:
           continue
    print(display)

    if guess not in chosen_word:
        print(f"\nYour Guess was incorrect :( {guess} is not in the word.")
        lives -= 1
        print(hang.stages[lives+1])
        if lives == -1:
            print("You Lose")
            quit()
print(f"YOU WIN, The guessed word was {chosen_word}")






