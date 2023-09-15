import random

# Get user input
user_input = input("Enter words or phrases separated by spaces: ")

# Split the input into words
words = user_input.split()

# Create a list of special characters, numbers, and letters
special_characters = "!@#$%^&*()_-+=<>?"
numbers = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialize an empty password
password = ""

# Iterate through the words and add a random character from each category
for word in words:
    if len(word) > 0:
        password += random.choice(word)  # Choose a character from the word
        password += random.choice(special_characters)  # Add a special character
        password += random.choice(numbers)  # Add a number
        password += random.choice(letters)  # Add a letter

# Shuffle the characters in the password
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print("Generated Password:", password)
