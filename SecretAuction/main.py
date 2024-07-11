from replit import clear
from art import logo
print(logo)
bids = {}
winner= {"name":"", "bid":int(0)}
print("Welcome to the secret auction program.")

other_bidders = False
def adding (person_name, value):
    bids[person_name]=value

while not other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    adding(name, bid)
    clear()

    if others=="no":
        other_bidders=True
        clear()

for key in bids:
    if bids[key]>winner["bid"]:
        winner["name"]= key
        winner["bid"] =bids[key]
print(f"The winner is {winner["name"]} with a bid of {winner["bid"]}")