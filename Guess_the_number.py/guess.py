# Guessing the number game

import random  # Random module
import sys


# STAGE 1  
print("Hello! What is your name?")  # Asks user for their name
name = input()  # Store the user's input in the name variable

print("Well, " +name+ ", I am thinking of a number between 1 & 20")
secretNumber = random.randint(1, 20)  # calling the randint dunction from the random module for a number between and including 1 & 20

# DEBUG
print("DEBUG: The secret number is actually " + str(secretNumber))

# STAGE 2
for guessesTaken in range(1, 7):  # for gueses taken between 1 & 7 (6 guesses)
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("""Your guess is too low.
               \n Guess another number""")
    elif guess > secretNumber:
        print("""Your guess is too high.
                \n Guess another number""")
    else:  # This condition is met when the user makes the correct guess
        break

print("-" * 50)
print("Game Results:")

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))

