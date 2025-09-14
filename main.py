import random

# The computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to 'Guess the Number'!")
print("I have a number in my mind between 1 and 100.")

while True:
    # Get the player's guess
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if the guess is correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.")
        break

print("Game over!")
