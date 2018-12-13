# Imports the 'randint' function from the 'random' module
from random import randint

# Imports the premade hangman.py file
from hangman import print_hang

def start_hangman():
    """Starts the game, if player chooses to play. Stores the final answer in
    a variable"""
    user_play_input = input('\nPlay Hangman? Type "y" to play: ')
    if user_play_input.lower() == 'y':
        user_word = initialize_game()
        return(user_word)
    else:
        print('\nYou did not type "y," exiting game.')
        exit_game()

def initialize_game():
    """Builds the final dictionary, chooses a random word"""
    print('\n<<<Starting game!>>>\n')
    final_list = populate_dictionary()
    return(choose_word(final_list))

def exit_game():
    """Exits the game based on user input"""
    exit()

def populate_dictionary():
    """Reads the text file, stores the words into a dictionary"""
    word_txt_file = open("words.txt","r")
    dictionary_list = word_txt_file.read().split('\n')
    # Create a new list, remove any words longer than 5 letters
    dict_shortened = []
    for index in dictionary_list:
        word_length = len(index)
        if word_length <= 5:
            dict_shortened.append(index)
    return(dict_shortened)

def choose_word(word_list):
    """Randomizes and returns an index number. Argument gets passed from the
    initialize_game() function."""
    random_index = randint(0,len(word_list))
    return(word_list[random_index])

def scoreboard(the_answer):
    """Creates the 'scoreboard' with the correct length, populates it with
    question marks."""
    scoreboard_list = []
    for letters in the_answer:
        scoreboard_list.append('?')
    print('Here is the length of the word:')
    print(scoreboard_list)
    return(scoreboard_list)

def take_user_input():
    """Takes the user input"""
    user_guess = input('\nGuess a letter: ')
    return(user_guess)

def correct_guess(letter, sboard_list, the_word):
    """User's letter guess is correct, modify the scoreboard accordingly"""
    current_index = 0
    # Iterate through each letter in the word, compare it to user's guess
    for each_letter in the_word:
        if letter == each_letter:
            # Change the value from '?' to the user's correct letter guess
            sboard_list[current_index] = letter
        current_index += 1

    # Win condition
    if '?' not in sboard_list:
        print('\nThe word is ' + the_word.upper() + '. You Win!')
        exit_game()
    else:
        print(sboard_list)

def incorrect_guess(guesses):
    print_hang(guesses)

####################################################################

# Store the final answer in a variable and start the game
the_final_answer = start_hangman()

# Creates the "Scoreboard" with the final answer word length
the_scoreboard = scoreboard(the_final_answer)

counter = 0
while counter != 7:
    guessed_letter = take_user_input()
    if guessed_letter in the_final_answer:
        correct_guess(guessed_letter, the_scoreboard, the_final_answer)
    else:
        incorrect_guess(counter)
        counter +=1
        # Print the answer when you lose
        if counter == 7:
            print('(The answer was ' + the_final_answer.upper() + ')')
