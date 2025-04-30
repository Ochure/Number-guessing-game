import random

def number_guessing_game():
    small_bound = 1
    high_bound = 100
    
    secret_number = random.randint(small_bound, high_bound)    
    
    #set the number of chances the user gets
    chances = 4
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 to 100")
    print(f'you have 5 chances to guess the correct number')
    while chances > 0:
        try:
            # Ask the user to make a guess
            guess = int(input(f"Guess a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

def difficulty_level():
    
    while True:
        # Ask the user to select difficulty level
        print("Select Difficulty Level:")
        print("1. Easy")
        print("2. Medium (default)")
        print("3. Hard")
        difficulty = input("Enter the number corresponding to your choice: ")
        