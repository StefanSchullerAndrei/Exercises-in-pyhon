# Number Guessing Game
# Concepts: Random numbers, conditionals, loops
# Description: Create a game where the user has to guess a number between 1 and 100, with hints if the guess is too high or too low.

import random
from art import logo

print(logo)



def game():

    print("I'm thinking of a number between 1 and 200.")

    selected_number_by_the_game = random.randint(1, 201)
    user_guess = None

    while user_guess != selected_number_by_the_game:
        user_guess = int(input("Please take a guess: "))

        if user_guess < selected_number_by_the_game:
            print("You need to go higher!")

        elif user_guess > selected_number_by_the_game:
            print("You need to go lower!")

        else:
            print("Hai ca esti bun lache!")


game()
