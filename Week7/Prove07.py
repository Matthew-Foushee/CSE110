import random

secret_word_options = []
with open("D:\Projects\School\CSE110\Week7\words.txt") as f:
  for line in f:
      secret_word_options.append(line[0:5])

random_index = random.randint(1, len(secret_word_options))

secret_word = secret_word_options[random_index]

print("Welcome to the word guessing game!")

guess_count = 0

while True:
    guess = input("What is your guess? ")
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue
    
    guess_count += 1

    if(guess == secret_word):
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break

    hint_output = "Your hint is: "

    for index in range(len(secret_word)):
        guess_letter = guess[index]
        secret_word_letter = secret_word[index]

        if guess_letter == secret_word_letter:
            hint_output += guess_letter.upper() + " "
        elif guess_letter in secret_word:
            hint_output += guess_letter + " "
        else:
            hint_output += "_ "

    print(hint_output)
