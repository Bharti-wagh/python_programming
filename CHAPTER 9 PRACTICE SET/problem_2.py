#2. The game() function in a program let's a user play a game and returns the score as an integer.You need to read file 
# 'Hi-scote.txt' .you need to write program to update the Hi-score whenever the game() function breaks the Hi-score.
# Example game function (just for demo, it returns a random score)
import random

def game():
    print("Game start")
    score = random.randint(1, 100)  
    print("Your Score:", score)

    with open("Hi-score.txt") as f:
        content = f.read()

    if content != "":
        hiscore = int(content)
    else:
        hiscore = 0

    # Update high score if needed
    if score > hiscore:
        print(" New High Score!")
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
    else:
        print("High Score remains:", hiscore)

# Run the game
game()
