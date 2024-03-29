name = input("Please input your name :")
age = input("Enter your age : ")
greeting = f"Hello there {name}. You are {age} years old which means you are eligible to use this program."
print(greeting)

import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of guesses
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while True:
        # Ask the player to guess the number
        guess = int(input("Enter your guess (between 1 and 100): "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == number_to_guess:
            print(f"Congratulations, {name}! You can read me mind and in only {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Start the game
guessing_game()
