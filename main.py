from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_finished = False
#function kto find highest nidding dict entry
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

  
while not bidding_finished:
  #ask user for name, then their bid
  name = input("What is your name?: \n")
  #change input to from str to int
  price = int(input("What is your bid?: $"))
  
  bids[name] = price
  
  should_continue = input("Are there any other users? Type 'yes' or 'no'. \n")
  if should_continue.lower() == "no":
    should_continue = True
    find_highest_bidder(bids)
    bidding_finished = True
  elif should_continue.lower() == "yes":
    clear()

