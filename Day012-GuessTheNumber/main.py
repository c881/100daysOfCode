# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

NUMBER_OF_GUESSES_EASY = 10
NUMBER_OF_GUESSES_NORMAL = 5
OUTPUTS = {1: "You won!", 0: "You Lost! better luck next time"}

remaining_guess = 0
low_value = 0
high_value = 100
keep_playing = True


def test_input(u_input):
    if u_input.isalpha():
        return -10
    if len(u_input) > 3:
        return -20
    return int(u_input)


print("Lets play a game of Guess the number")
number_to_guess = random.randint(0, 100)
hardness = input("Type 'E' for an easy game or 'H' for Hard game: ")
if hardness in ('e', 'E'):
    remaining_guess = NUMBER_OF_GUESSES_EASY

if hardness in ('h', 'H'):
    remaining_guess = NUMBER_OF_GUESSES_NORMAL
guessed = -1
print(f"testing purpos, number picked: {number_to_guess}")
while keep_playing and remaining_guess > 0:
    user_input = input("pick a number between 0 and 100, -1 to quit: ")
    guessed = test_input(user_input)
    if guessed == -1:
        keep_playing = False
    # user guessed a number between 0 and 100
    if low_value <= guessed <= high_value:
        remaining_guess -= 1
        if guessed > number_to_guess:
            high_value = guessed
            print("To high!")
        elif guessed < number_to_guess:
            low_value = guessed
            print("To low!")
        elif guessed == number_to_guess:
            keep_playing = False
    elif guessed == -10:
        print("I have asked you for a number")
    elif guessed == -20:
        print("I have asked you for a number between 0 and 100")

if remaining_guess >= 0 and guessed == number_to_guess:
    print(OUTPUTS[1])
else:
    print(OUTPUTS[0])