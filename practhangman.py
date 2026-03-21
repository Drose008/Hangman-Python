# import required libraries
import pandas as pd        # for reading dataset
import random              # for random word selection


# hangman drawing stages (from empty to full)
hangman_stages = [

"""
   -----
   |   |
       |
       |
       |
       |
---------
""",

"""
   -----
   |   |
   O   |
       |
       |
       |
---------
""",

"""
   -----
   |   |
   O   |
   |   |
       |
       |
---------
""",

"""
   -----
   |   |
   O   |
  /|   |
       |
       |
---------
""",

"""
   -----
   |   |
   O   |
  /|\\  |
       |
       |
---------
""",

"""
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
---------
""",

"""
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
---------
"""
]


# function to filter words based on difficulty level
def choose_words_by_level(words, level):
    filtered_words = []

    for word in words:

        # easy → small words
        if level == "easy" and len(word) <= 5:
            filtered_words.append(word)

        # normal → medium words
        elif level == "normal" and 6 <= len(word) <= 9:
            filtered_words.append(word)

        # hard → long words
        elif level == "hard" and len(word) > 9:
            filtered_words.append(word)

    return filtered_words


# main game function
def hangman():

    # load dataset (keep words.csv in same folder)
    data = pd.read_csv("words.csv")

    # convert words column to list and remove empty values
    words = data["word"].dropna().tolist()

    print("\n🎮 Welcome to Hangman!")
    print("Try to guess the word before you run out of tries.\n")

    # difficulty selection
    level = input("Choose difficulty (easy / normal / hard): ").lower()

    # filter words based on level
    filtered_words = choose_words_by_level(words, level)

    # fallback if no words found
    if len(filtered_words) == 0:
        print("No words found for this level. Using all words.")
        filtered_words = words

    # choose random word
    word = random.choice(filtered_words).lower()

    guessed_letters = []     # store guessed letters
    tries = 6                # total attempts
    wrong_guesses = 0        # track wrong guesses
    hint_used = False        # allow only one hint

    print("\nThe word has", len(word), "letters.")

    game_over = False

    # game loop
    while not game_over:

        guess = input("\nGuess a letter: ").lower()

        # input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # check repeated guess
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # build display word
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        # if guess is wrong
        if guess not in word:

            tries -= 1
            wrong_guesses += 1

            print("Wrong guess!")
            print(hangman_stages[wrong_guesses])
            print("Tries left:", tries)

            # hint system (only once)
            if not hint_used:
                hint = input("Do you want a hint? (y/n): ").lower()

                if hint == "y":

                    remaining_letters = []

                    for letter in word:
                        if letter not in guessed_letters:
                            remaining_letters.append(letter)

                    if len(remaining_letters) > 0:
                        hint_letter = random.choice(remaining_letters)
                        print("Hint: new letter added:", hint_letter)

                        guessed_letters.append(hint_letter)

                        # update display after hint
                        display = ""
                        for letter in word:
                            if letter in guessed_letters:
                                display += letter + " "
                            else:
                                display += "_ "

                        print("\nWord:", display)

                    else:
                        print("No hints available!")

                    hint_used = True

            else:
                print("No hints available")

        # win condition
        if "_" not in display:
            print("\n🎉 Congratulations! You guessed the word:", word)
            game_over = True

        # lose condition
        if tries == 0:
            print("\n💀 Game Over! The word was:", word)
            game_over = True


# main loop to replay game
def true():
    while True:
        hangman()

        choice = input("\nPlay again? (y/n): ").lower()
        if choice != "y":
            print("Thanks for playing! 👋")
            break


# start the game
true()
