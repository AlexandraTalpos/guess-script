#a small-scale game for a computer player to guess a random number

import random #This will allow us to reference, or use, all of the command definitions defined in this module

number_to_guess = 0 #This will hold the number that the user has to guess.
num_guesses = 5 #This will represent how many tries the user gets to guess the correct number before the game ends

number_to_guess = random.randint(1,10)
while (num_guesses > 0):
    print("Guess a number between 1 and 10!")
    response = random.randint(1, 10) #generate the computer player's guess
    response_str = str(response)
    print("You guessed: " + str(response_str))
    num_guesses -= 1
    if response == number_to_guess:
        print("Congratulations, you guessed the number!")
        break
    elif response < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
if num_guesses == 0:
    print("Sorry, you didn't guess the number.")
    number_to_guess = str(number_to_guess)
    print("The correct number was " + number_to_guess)
            
