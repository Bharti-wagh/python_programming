import random

options = ['snake', 'water', 'gun']
computer = random.choice(options)
user = input("Enter your choice (snake/water/gun): ").lower()

if user == computer:
    print("It's a tie!")
elif (user == 'snake' and computer == 'water') or \
     (user == 'water' and computer == 'gun') or \
     (user == 'gun' and computer == 'snake'):
    print("You win!")
else:
    print("You lose!")

print(f"Computer chose: {computer}")

