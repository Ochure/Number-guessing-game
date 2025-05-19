import random
import time  # Import the time module for the timer
    
def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("🔢 I'm thinking of a number between 1 and 100.")
    print("🕒 You have 5 attempts to guess the correct number.")
    
def number_guessing_game_with_timer():
    small_bound = 1
    high_bound = 100
    
    
def difficulty_level():
        print("Choose a difficulty level:")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            return 1, 10
        elif choice == '2':
            return 1, 50
        elif choice == '3':
            return 1, 100
        else:
            print("Invalid choice. Defaulting to Hard level (1-100).")
            return 100
        
def play_game():
    lower_bound, upper_bound = difficulty_level()
    
    
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = 5
    attempts_used = 0

    print(f"\n🔢 I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"🕒 You have {max_attempts} attempts to guess it.\n")

    start_time = time.time()

    while attempts_used < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts_used + 1}: Enter your guess: "))
            attempts_used += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"⚠️ Please enter a number between {lower_bound} and {upper_bound}.")
                continue

            if guess == secret_number:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                print(f"🎉 Correct! You guessed the number in {attempts_used} attempt(s) and {time_taken} seconds.")
                break
            elif guess < secret_number:
                print("⬆️ Too low! Try again.")
            else:
                print("⬇️ Too high! Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    else:
        print(f"😞 You've used all your attempts. The number was {secret_number}.")

    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        print("\nRestarting game...\n")
        play_game()
    else:
        print("👋 Thanks for playing! Goodbye.")
        

# Start the game
play_game()
