import random

def guess_the_number():
    # Select a random number in the desired range
    min_range = 1
    max_range = 100  # You can adjust this range as needed
    secret_number = random.randint(min_range, max_range)
    
    score = 100  # Starting score
    
    print("Welcome to Guess the Number Game!")
    print(f"I'm thinking of a number between {min_range} and {max_range}.")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            
            # Compare the user's guess with the secret number
            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number: {secret_number}")
                print(f"Your final score is: {score}")
                break
            elif user_guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
            
            # Reduce the score with each incorrect guess
            score -= 10
            
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    guess_the_number()
