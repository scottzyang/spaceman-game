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
    # open words.txt file to read only
    f = open('words.txt', 'r')

    # read lines from file into words_list variable
    words_list = f.readlines()
    f.close()
    
    # split the words list by the space
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line

    # select a random word from list
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
    while (is_letter_guessed):
        for letter in secret_word: 
            # if letter is found in the letters guessed, continue the while loop
            if letter in letters_guessed:
                is_letter_guessed = True
            else:
                # if letter is not in letters guessed, return false to the function
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
    
    # loop through each letter in the secret word
    for letter in secret_word:
        # if the letter exists in the letters guessed list, add that letter to the empty string
        if letter in letters_guessed:
            word_status += letter
        else:
            # if it does not exist, replace it with the _
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
        print("Correct guess!\n")
        return True
    else:
        print("Incorrect guess!\n")
        return False

# function to restart game
def restart_game():
    # prompt if user wants to play again
    play_again = input("Would you like to play again? (yes or no) ")
    # if yes, clear the console, and call following functions to restart the game
    if play_again == "yes":
        os.system('clear')
        secret_word = load_word()
        spaceman(secret_word)
        # If user chooses to not continue, call stack returns here and returns false to end game
        return False
    else:
        # if no, return false to end the game
        return False

# function to draw the spaceman figure
def ascii_art(level):
    #dictionary containing key-value pairs with a drawing
    spaceman_drawing = {
        0: '',
        1: ' o\n',
        2: ' o\n  \\\n',
        3: ' o\n |\\\n',
        4: ' o\n/|\\\n',
        5: ' o\n/|\\\n  \\\n',
        6: ' o\n/|\\\n/ \\\n',
        7: ' o\n/|\\\n/ \\\n:( GAME OVER\n'

    }
    return spaceman_drawing[level]


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    letters_guessed = ''
    guesses = 7
    rounds = 1
    number_incorrect = 0

    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")

    # prompt user for instructions
    instructions = input("Would you like instructions on how to play? (yes or no): ")
    if instructions == 'yes':
        print("\nWe will select a random word, and you will input a single letter guess at a time\nto try and figure out the word. You only get 7 incorrect guesses\nbefore the game ends, so make sure you choose wisely!")
        # prompt user if they are ready to play
        play_time = input('\nReady to play? (yes or no): ')
        # if no, end the game
        if play_time == 'no':
            return
        else:
            # if yes, clear the console and start game
            os.system('clear')
    else:
        # is user opts for no instructions, clear the console and start game
        os.system('clear')

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    # continue while guesses are greater than 0
    while (guesses > 0):
        print(f"\nRound {rounds}\nYou have {guesses} guesses left!")
        user_input = True

        # evaluate validity of guess
        while user_input:
            guess = input(f"Input your guess here: ")
            # if user guess is not a letter or is more than one character, reprompt
            if not guess.isalpha() or len(guess) > 1:
                print('\nInvalid guess, try again!')
            # if letter has been guessed, reprompt user
            elif guess in letters_guessed:
                print('\nLetter already guessed!')
            # if letter has not, add letter to the letters_guessed string, and stop the loop/continue game
            else:
                letters_guessed += guess
                user_input = False
        os.system('clear')
        print(f"Letters guessed so far: {letters_guessed}\n")
        
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        # if guess is not in secret word
        if not is_guess_in_word(guess, secret_word):
            # decrease guesses by 1
            guesses -= 1
            # increment number incorrect by 1
            number_incorrect += 1
            # pass number_incorrect as key and return the value, value is the ascii art of spaceman
            print(ascii_art(number_incorrect))
        else:
            # if correct, print nothing for ascii art
            print(ascii_art(number_incorrect))

    #TODO: show the guessed word so far
        # display the current guessed word and blank spaces
        print(get_guessed_word(secret_word, letters_guessed))

    #TODO: check if the game has been won or lost
        if (is_word_guessed(secret_word, letters_guessed)):
            print(f"\nCongrats! You completed the word with {guesses} guesses remaining. The word was '{secret_word}'.")
            # if user chooses to restart, continue. Else end game
            if (restart_game()):
                continue
            else:
                return

        # increment the round value to keep track of rounds
        rounds += 1

    ## outside of for loop
    print(f"\nYou have {guesses} guesses left! The word was '{secret_word}'. Please try again!")
    #reprompt user if they want to play again
    restart_game()


#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
