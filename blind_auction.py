import auction_art
import os
print(auction_art.logo)
print("Welcome to the secret auction program")

go_again = True
auction = {}

def clear():
    os.system('cls')

def find_highest_bid(bidding_record):
    highest_bid = 0
    for bidder in bidding_record: #Loop through keys in dictionary  
        bid_amount = bidding_record[bidder] #Save value of key in bid_amount variable
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

    
while go_again:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    auction[name] = bid
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if more_bidder == "no":
        go_again = False
        find_highest_bid(auction)
    elif more_bidder == "yes":
        clear()
        



