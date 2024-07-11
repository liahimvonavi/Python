from art import logo, vs
from game_data import data
import random
from replit import clear
def game():
    score =0
    print (logo)
    game_should_continue=True
    acc_b = random.choice(data)
    while game_should_continue:
        acc_a = acc_b
        acc_b = random.choice(data)
        if acc_a==acc_b:
            acc_b = random.choice(data)

        def format_data(acc):
            account_name = acc["name"]
            account_descr = acc["description"]
            account_country = acc["country"]
            return f"{account_name}, a {account_descr}, from {account_country}"
        def check_answer(guess, a_follower, b_follower):
            if a_follower>b_follower:
             return guess == "a"
            else:
                return guess == "b"
        print(f"Compare A: {format_data(acc_a)}")
        print(vs)
        print(f"Against B: {format_data(acc_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = acc_a["follower_count"]
        b_follower_count = acc_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        clear()
        print(logo)
        if is_correct:
            score+=1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue=False
            print(f"Sorry that is wrong. Final score: {score}")
game()
