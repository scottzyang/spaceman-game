from asyncio import format_helpers
from json import load
from operator import truediv
import random
import os

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Loop through the secret_word and see if letters in secret_word are in letters_guessed
        - Return true if  all letters are in letters_guessed, meaning word is guessed
        - Return false if all letters not in 

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    is_letter_guessed = True

    # loop through each letter of the secret word
    while (is_letter_guessed == True):
        for letter in secret_word: 
            # if letter is found in the letters guessed, continue the loop
            if letter in letters_guessed:
                is_letter_guessed = True
            else:
                # if letter is not in letters guessed, return false to the function
                is_letter_guessed = False
                return False
        # If each letter is found, return true to the function
        return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores 
    for letters that have not been guessed yet.



    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the 
        string should contain the letter at the correct position.  For letters in the word that the user has 
        not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have 
    # been guessed correctly so far that are saved in letters_guessed and underscores for 
    # the letters that have not been guessed yet
    word_status = ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            word_status += letter
        else:
            word_status += '_'
    return(word_status)
            


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        print("Correct guess!")
        return True
    else:
        print("Incorrect guess!")
        return False

# function to restart game
def restart_game():
    play_again = input("Would you like to play again? (yes or no) ")
    if play_again == "yes":
        secret_word = load_word()
        spaceman(secret_word)
        return False
    else:
        return False

def ascii_art(level):
    if level == 0:
        print(' o\n')
    elif level == 1:
        print(' o\n  \\\n')
    elif level == 2:
        print(' o\n |\\\n')
    elif level == 3:
        print(' o\n/|\\\n')
    elif level == 4:
        print(' o\n/|\\\n  \\\n')
    elif level == 5:
        print(' o\n/|\\\n/ \\\n')
    else:
        print(' o\n/|\\\n/ \\\n:(')
    '''
     o\n`
    /|\\\n
    / \\\n   
    :(
    '''


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    letters_guessed = ''
    guesses = 7

    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman! We will select a random word, and you'll have 7 letter guesses to complete the word")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    #while (guesses > 0):
    for level in range(7):
        print(f"You have {guesses} guesses left!")
        guess = input(f"Input your guess here: ")
        guesses -= 1
        letters_guessed += guess
        os.system('clear')
        
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        is_guess_in_word(guess, secret_word)

    #TODO: show the guessed word so far
        ascii_art(level)
        print(get_guessed_word(secret_word, letters_guessed))

    #TODO: check if the game has been won or lost
        if (is_word_guessed(secret_word, letters_guessed)):
            print(f"Congrats! You completed the word with {guesses} guesses remaining. The word was {secret_word}.")
            if (restart_game()):
                continue
            else:
                return

    ## outside of for loop
    print(f"You have {guesses} guesses left! Please try again!")
    restart_game()


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
