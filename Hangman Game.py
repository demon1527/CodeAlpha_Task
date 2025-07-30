import random

words = ["apple", "banana", "grape", "orange", "melon"]
secret_word = random.choice(words)

guessed_letters = []
tries = 6
display = ""

for letter in secret_word:
    display += "_"

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.") 
print("You have", tries, "tries.\n")

while tries > 0:
    print("Word:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!\n")
        new_display = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                new_display += guess
            else:
                new_display += display[i]
        display = new_display
    else:
        print("Wrong guess!")
        tries -= 1
        print("Tries left:", tries, "\n")

    if "_" not in display:
        print("You won! The word was:", secret_word)
        break

if "_" in display and tries == 0:
    print("Game over! The word was:", secret_word)