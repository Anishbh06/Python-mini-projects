import os
import biddinglogo


clear = lambda: os.system('cls')
clear()

print("SECRET AUCTION GAME")
print(biddinglogo.logo)
list = {}
ans = "yes"
while ans != "no":
   name = input("ENter your name: ")
   amount = input("Enter your amt: ")
   list[name] = amount
   ans = input("Wanna continue yes or no").lower()
   
   
def highest(list):
   max = 0
   highest_bidder = ""
   for key in list:
      clear()
      value = int(list[key])
      if value > max:
         max = value
         highest_bidder = key
   return highest_bidder, max
    
    
highest_bidder , max = highest(list)
print(f"\nHighest bidder: {highest_bidder} and amount:{max}")

      



   