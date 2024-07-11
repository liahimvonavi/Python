import random
import asciiImage
import words
print(f"{asciiImage.logo}\n")
chosen_word = random.choice(words.word)
shown_word = ["_"] *(len(chosen_word))
same_input = []
lives = 7
while "_" in shown_word:
    print("The Word is: " +' '.join(shown_word))
    guessed = input("Guess a letter: \n").lower()
    if len(guessed)==1:

        if guessed in same_input:
            print("You have already picked this letter try again with another one.")

        else:
            same_input.append(guessed)
            if guessed in chosen_word:
                for index, letter in enumerate(chosen_word):

                    if letter==guessed:
                        shown_word[index]=letter

            else:
                lives-=1

                print(asciiImage.stages[lives])
                if lives == 0:
                    print(f"The word was: {''.join(chosen_word)}")
                    print("You Lose!Game Over!")
                    exit()
    else:
        print("Invalid input!You can only choose one letter at a time!")
print(f"The word is: {''.join(chosen_word)}\n")
print("You Win ")