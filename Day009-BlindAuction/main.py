from os import system, name
from art import logo

# HINT: You can call clear() to clear the output in the console.


def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')


auction = {}
more_bidders = "yes"
print(logo)
print("Welcome to the secret auction program")
while more_bidders == "yes":
    bidder_name = input("What is your name? ")
    bidding = round(float(input("what is your bid? $")), 2)
    auction[bidder_name] = bidding
    more_bidders = input("Are there any other bidders? type 'yes' or 'no'\n").lower()
    clear()
top_bidder = ""
top_bidding = -1
for bidder in auction:
    if auction[bidder] > top_bidding:
        top_bidding = auction[bidder]
        top_bidder = bidder
print(f"The winner is {top_bidder} with a bid of ${top_bidding}")
