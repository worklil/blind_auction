# from replit import clear

# HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bids = {}
bids_finished = False


def find_highest_biddin(biddin_record):
    highest_bid = 0
    for bidder in biddin_record:
        bid_amount = biddin_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bit of ${highest_bid}")


while not bids_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    result = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if result == 'no' or result == 'No':
        bids_finished = True
        find_highest_biddin(bids)
    elif result == 'yes' or result == 'Yes':
        bids.clear()
