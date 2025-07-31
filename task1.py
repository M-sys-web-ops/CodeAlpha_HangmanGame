import random

# Defining a list of predefined words
words = ["banana", "tomato", "potato", "apple", "mango"]

# Randomly selected word from the list
secret_word = random.choice(words)
guessed_word = "_" * len(secret_word)
incorrect_guesses = 0
max_incorrect = 6
previous_guesses = []

# Func to display current state of guessed word
def display_state(guessed_word):
    print("Current word: ", " ".join(guessed_word))
    print("Incorrect guesses: ", incorrect_guesses, "/", max_incorrect)

# Main game loop
while incorrect_guesses < max_incorrect and "_" in guessed_word:
    display_state(guessed_word)
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue
    if guess in previous_guesses:
        print("You've already guessed that letter.")
        continue

    previous_guesses.append(guess)

    if guess in secret_word:
        print("Good guess!")
        guessed_word = "".join(
            [secret_word[i] if secret_word[i] == guess else guessed_word[i] for i in range(len(secret_word))]
        )
    else:
        incorrect_guesses += 1
        print("Incorrect guess.")

# End of the game
if "_" not in guessed_word:
    print("Congratulations! You've guessed the word: ", secret_word)
else:
    print("Sorry, you've lost! The word was: ", secret_word)