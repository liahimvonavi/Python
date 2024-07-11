from art import logo
import random
from replit import clear
def deal_card():
    """Returns a random cards from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, cpu_score):
    """compare scores"""
    if user_score == cpu_score or cpu_score == 0 and user_score == 0:
        return "Draw"
    elif cpu_score == 0:
        return "Computer has a BlackJack"
    elif user_score == 0:
        return "YOU WIN Nice BlackJack"
    elif user_score > 21:
        return "You Lose too many "
    elif cpu_score > 21:
        return "YOU WIN Computer went over"
    elif user_score > cpu_score:
        return "YOU WIN"
    else:
        return "You Lose"
def play_game():
    print(logo)
    player_cards = []
    cpu_cards = []
    for _ in range(2):
        player_cards.append(deal_card())
        cpu_cards.append(deal_card())
    is_game_over = False

    while is_game_over == False:
        user_score = calculate_score(player_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"Your cards: {player_cards}, current score: {user_score}")
        print(f"Computer's first card: {cpu_cards[0]}")
        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            get_anotherCard = input("Type 'y' to get another card , type 'n' to pass: ").lower()
            if get_anotherCard == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)
    print(f"Your final hand: {player_cards}, final score: {user_score}")
    print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare(user_score, cpu_score))
while input("Do you want to play a game of BlackJack Type 'y' or 'n': \n") == "y":
    clear()
    play_game()