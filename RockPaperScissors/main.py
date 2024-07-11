import images
import random
vizualisationOfTheChoice = [images.rock , images.paper, images.scissors]
user_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
correctInput = [0, 1, 2]
if user_choice not in correctInput:
    print("Incorrect Input")
    exit()

computer_choice = random.randint(0, 2)
print(f"You chose{vizualisationOfTheChoice[user_choice]}\n")
print(f"Computer chose{vizualisationOfTheChoice[computer_choice]}\n")

if user_choice==0 and computer_choice==2:
    print("You win")
elif user_choice==2 and computer_choice==0:
    print("You lose!")
elif user_choice>computer_choice:
    print("You win!")
elif computer_choice>user_choice:
    print("You lose!")
elif user_choice==computer_choice:
    print("Draw")

