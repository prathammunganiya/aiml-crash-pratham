import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Guess a number between 1 and 100")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break

if guess != secret_number:
    print(f"Game Over! The correct number was {secret_number}")