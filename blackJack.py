import random
import os

clear = lambda: os.system('cls')
clear()

players_cards = []
computers_cards = []
def new_game():
   if input(" Press n if you want to start a new game or press q to quit: ") == "n":
      blackjack()
   else:
      quit()
def computersChoice():
        global players_cards, computers_cards
        computers_another_cards = deal_card()
        computers_cards.append(computers_another_cards)
        computers_value = sum(computers_cards)
        return computers_cards,  computers_value
def checkWinner(users_value, computers_value):
     if users_value == computers_value:
         print("It's a Tie ")
         new_game()
     if users_value < 21 and computers_value < 21:
      if users_value > computers_value:
       print("You Win!!\n")
       new_game()
      else:
        print("You Lose\n")
        new_game()
               
     if users_value > 21 and computers_value < 21:
      print("You lose\n")
            
     elif computers_value > 21 and users_value < 21:
      print("You win!!")
def deal_card():
     deck_cards = [10,2,3,4,5,6,7,8,9,10,10,10,10]
     return random.choice(deck_cards)   
def blackjack():     
 clear()
 global players_cards , computers_cards
 players_cards = []
 computers_cards = []

 start = input("Do You want to play a game of Black Jack.\n Press y: Yes\n Press n: No \n ")
 if start == "y":
    print("************WELCOME TO BLACK JACK*****************")

        #users first choice
    players_cards.append(deal_card())
    players_cards.append(deal_card())    
    value = sum(players_cards)
    print(f"\nYour deck of cards contain {players_cards}, score = {value}\n")

        #computers first choice
    computers_cards.append(deal_card())
    print(f"Computer's conatins= {computers_cards}, score = {computers_cards[0]}\n")

        #asking to choose to deal or pass  
    ans = input("Type y to deal another card or n to pass: ")

    if ans == "y":
        clear()
        # users second choice
        players_cards.append(deal_card())
        users_value = sum(players_cards)
        print(f"\nYour deck of cards contain {players_cards}, score = {users_value}\n")

        #computers second choice         
        computers_cards , computers_value = computersChoice()
        print(f"Computers deck of cards = {computers_cards}, score = {computers_value}\n")

    #check for winner
        checkWinner(users_value,computers_value)
        
    elif ans == "n":
        clear()    
        print(f"\nYour deck of cards contain {players_cards}, score = {value}\n")
        #computers second choice
        computers_cards , computers_value = computersChoice()
        print(f"Computers deck of cards = {computers_cards}, score = {computers_value}\n")

        #check for winner
        checkWinner(value,computers_value)
    else:
        quit()

 
blackjack()