import random
import sys
from termcolor import colored
import nltk

from nltk.corpus import words


def print_menu():
    print("Let's play Wordle!")
    print("Type a five (5) letter word and hit enter!\n")

def read_random_word():
    with open("/users/alex/documents/vscode/wordle/words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)
    
nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print_menu()
play_again = ""
while play_again != "q":
    #word = read_random_word()
    word = random.choice(words_five)
    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        correct_positions = []  # List to store correct positions
        wrong_positions = []    # List to store wrong positions

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                correct_positions.append(i)
            elif guess[i] in word:
                wrong_positions.append(i)

        for i in range(min(len(guess), 5)):
            if i in correct_positions:
                print(colored(guess[i], 'green'), end="")
            elif i in wrong_positions:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()
            
        if guess == word:
                print(colored(f"Congrats! You got the Wordle in {i} guesses", 'red'))
                break
        elif attempt == 6:
            print(f"Sorry, the Wordle was...{word}")
            
    play_again = input("Want to play again? Type q to exit")
