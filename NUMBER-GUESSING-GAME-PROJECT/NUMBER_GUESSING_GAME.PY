import random
number_to_guess = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Higher number please!")
    elif guess > number_to_guess:
        print("Lower number please!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
