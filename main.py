from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the SILENT AUCTION, where the gavel always Drops!!")

bids = {}


#here's a ~function~ for making a bid!
def make_bid(user_name, user_bid):
    bids[user_name] = user_bid

#ask if there's another user and, if so, take their bid. 
more_bidders = True
while more_bidders == True:
    make_bid(input("What is your name?\n"), input("What is your bid?\n"))
    yes_or_no = input(
        "Will someone else be bidding after you? Type yes or no.\n")
    if yes_or_no == "yes":
        more_bidders = True
        clear()
    elif yes_or_no == "no":
        more_bidders = False

#calculate and display the winner's name and bid! 
else:
    winner_name = max(bids, key=bids.get)
    winner_bid = max(bids.get(winner_name))
    print(f"The winner is {winner_name}, with a bid of ${winner_bid}!")
