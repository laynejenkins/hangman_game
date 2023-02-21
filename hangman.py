import random
import os

from hangman_art import stages, logo
from hangman_word_list import word_list

print(logo)

# Game selects a random word from the dictionary
chosen_word = random.choice(word_list)

# Create the "_""_""_" GUI.
display = []
for letter in chosen_word:
    display += "_"

lives = 6
used_guesses = []


def guess_checker(chosen_word, guess):
    # Check if guessed letter is in word. If so, display that letter in GUI.
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
            print("Nice! '{guess}' is in the word!")
    # If guess is not in word, lose 1 life and advance hangman with extra limb.
    if guess not in chosen_word:
        print(
            f"Sorry, '{guess}' is not in the word. You lose a life.")
        lives -= 1


# Game Logic
while "_" in display and lives > 0:
    print(stages[lives])
    print(display)
    print(f"Used letters: {used_guesses}")
    guess = input("Please choose a letter: ").lower()
    os.system('cls||clear')
    # See if letter has already been guessed. Doesn't count against lives.
    if guess in used_guesses:
        print(f"You have already guessed '{guess}'.")
        continue
    used_guesses.append(guess)
    guess_checker(chosen_word, guess)
    # Game over!
    if lives == 0:
        print(stages[lives])
        print(f'You lose! The word was "{chosen_word}".')
        break
