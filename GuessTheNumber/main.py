from art import logo
import random
EASY_TURNS = 10
HARD_TURNS = 5
def difficulty():
    diff_choice = input("Choose a difficulty. Type 'easy' or 'hard'\n").lower()
    if diff_choice == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS
def check_answer(guess, the_number, lifes):
    if guess > the_number:
        print("Too high.")
        return lifes - 1

    elif guess < the_number:
        print("Too low.")
        return lifes - 1
    else:
        print(f"You got it! The answer was {the_number}")
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    the_number = random.randint(1, 100)
    lifes = difficulty()
    guess = 0
    while guess != the_number:
        print(f"You have {lifes} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lifes = check_answer(guess, the_number, lifes)
        if lifes == 0:
            print("You have ran out of guesses, you loose.")
            return
        elif guess!= the_number:
            print("Guess again.")
game()