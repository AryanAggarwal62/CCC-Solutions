# Name: Aryan Aggarwal, id. 898707
# Description: This program will play a guessing game with the user. The user
#              will guess numbers that the computer has chosen. The user 
#              can also select the difficulty (number of guesses). The game
#              ends when the user guesses correctly or the number of guesses
#              runs out.

# import necessary libraries
import random

# Initialize variables
difficulty_asking = True
playing = True
game_restart_loop = True
num_guesses = 0

# Welcome the user and provide instructions
print('Welcome to the Number Guessing Game!')
print('I will come up with a number between 1-100, and you will guess it when '\
      'prompted.')
print('If your guess is incorrect, I will tell you if your guess is too high '\
      'or too low.')
print('When prompted for the difficulty, select E for Easy (15 guesses), '\
      'M for Medium (10 guesses), or H for Hard (5 guesses)')

# Ask the user to select a difficulty and check for valid input
while difficulty_asking:
    try:
        difficulty = (input('Select a difficulty: '))
        if difficulty == 'E' or difficulty == 'M' or difficulty == 'H':
            difficulty_asking = False
        else:
            print('Invalid input, try again.')
    except:
        print('Invalid input, try again.')
        
# Set the number of guesses based on the users chosen difficulty
if difficulty == 'E':
    max_guesses = 15
elif difficulty == 'M':
    max_guesses = 10
elif difficulty == 'H':
    max_guesses = 5

# Loop to restart the game if the user wants to play again
while game_restart_loop:
    # Resetting the game variables
    playing = True
    num_guesses = 0
    
    # Computer chooses a random number between 1-100
    random_number = random.randint(1, 100)
    print(random_number)
    # Game loop that allows the user to make guesses
    while playing:
        try:
            # Prompt the user for a guess
            guess = int(input("Guess the number (You have "\
                              f"{max_guesses - num_guesses} guesses left): "))
            
            # Check if the guess is correct, too high, or too low
            if guess == random_number:
                print("Congratulations! You've guessed the " \
                      f"number {random_number} correctly!")
                final_guesses = num_guesses + 1
                if final_guesses == 1:
                    print(f"It took 1 guess to guess the correct answer!")
                else:
                    print(f"It took {final_guesses} guesses to guess " \
                          "the correct answer!")
                playing = False
            elif guess > random_number:
                print("Too high!")
                num_guesses += 1
            elif guess < random_number:
                print("Too low!")
                num_guesses += 1
                
            # Check if the player has run out of guesses
            if num_guesses == max_guesses:
                print("You've run out of guesses! The correct number "\
                      f"was {random_number}.")
                playing = False
                
        except:
            print("Please enter a valid number.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        game_restart_loop = False

  

