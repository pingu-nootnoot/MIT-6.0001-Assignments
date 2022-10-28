# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    i = 0
    while i < len(secret_word):
        char = secret_word[i]
        if char in letters_guessed:
            i += 1
        else:
            i += 1
            flag = False
    return flag

#secret_word = 'apple'
#letters_guessed = ['p', 'a', 'e', 'l', 'e', 'd']
#print(is_word_guessed(secret_word, letters_guessed) )

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    res = []
    while i < len(secret_word):
        char = secret_word[i]
        if char in letters_guessed:
            res.append(secret_word[i])
            i += 1
        else:
            res.append("_ ")
            i += 1
    my_word = "".join(res)
    return my_word

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#letters_guessed = ['p', 'a', 'e', 'l', 'e', 'd']

#print(get_guessed_word(secret_word, letters_guessed) )



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list(string.ascii_lowercase)
    available_letters = []
    for char in alphabet:
        if char not in letters_guessed:
            available_letters.append(char)
    return "".join(available_letters)
    
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))

    

def warnings(warnings_remaining, user_input, letters_guessed, secret_word):
    '''
    warnings_remaining = 3 initial value
    In following, warning_count -= 1
        invalid
        already guessed
    When warnings_remaining = 0 and input_guess invalid/already guessed,
    only print warnings and return warnings_remaining == 0
    '''
    flag = True
    if warnings_remaining > 1:
        if str.isalpha(user_input) == True and len(user_input) == 1:
            if user_input not in letters_guessed:
                flag = True
                return flag
            else:
                flag = False
                print("Oops! You've already guessed that letter. You now have", warnings_remaining - 1, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                return flag
        elif user_input == '*':
            flag = True
            return flag
        else:
            flag = False
            print("That is not a valid letter. You have", warnings_remaining - 1, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            return flag
    if warnings_remaining == 1:
        if str.isalpha(user_input) == True and len(user_input) == 1:
            if user_input not in letters_guessed:
                flag = True
                return flag
            else:
                flag = False
                print("Oops! You've already guessed that letter. You now have 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
                return flag
        elif user_input == '*':
            flag = True
            return flag
        else:
            flag = False
            print("That is not a valid letter. You have 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
            return flag
    if warnings_remaining <= 0:
        if str.isalpha(user_input) == True and len(user_input) == 1:
            if user_input not in letters_guessed:
                flag = True
                return flag
            else:
                flag = False
                print("Oops! You've already guessed that letter. You now have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                return flag
        elif  user_input == '*':
            flag = True
            return flag
        else:
            flag = False
            print("That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            return flag
        
#def hangman(secret_word):
#    '''
#    secret_word: string, the secret word to guess.
#    
#    Starts up an interactive game of Hangman.
#    
#    * At the start of the game, let the user know how many 
#      letters the secret_word contains and how many guesses s/he starts with.
#      
#    * The user should start with 6 guesses
#
#    * Before each round, you should display to the user how many guesses
#      s/he has left and the letters that the user has not yet guessed.
#    
#    * Ask the user to supply one guess per round. Remember to make
#      sure that the user puts in a letter!
#    
#    * The user should receive feedback immediately after each guess 
#      about whether their guess appears in the computer's word.
#
#    * After each guess, you should display to the user the 
#      partially guessed word so far.
#    
#    Follows the other limitations detailed in the problem write-up.
#    '''
#    # FILL IN YOUR CODE HERE AND DELETE "pass"    
#    
#    warnings_remaining = 3
#    guesses_remaining = 6
#    letters_guessed = []
#    vowels = ['a', 'e', 'i', 'o', 'u']
#    print("Welcome to the game Hangman! \nI am thinking of a word that is", len(secret_word), "letters long. \nYou have 3 warnings left. \n-------------")
#    print("You have", guesses_remaining, "guesses left.")
#    print("Available letters: " + get_available_letters(letters_guessed))
#    while guesses_remaining > 0:
#        user_input = str.lower(input("Please guess a letter: "))
#        flag = warnings(warnings_remaining, user_input, letters_guessed, secret_word)
#        if flag == True:
#            letters_guessed.append(user_input)
#            if user_input in secret_word:
#                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
#                if is_word_guessed(secret_word, letters_guessed) == False:
#                    print("-------------")
#                    print("You have", guesses_remaining, "guesses left.")
#                    print("Available letters: " + get_available_letters(letters_guessed))
#                if is_word_guessed(secret_word, letters_guessed) == True:
#                    print("-------------")
#                    print("Congratulations, you won! Your total score for this game is:", guesses_remaining*len(set(secret_word)))
#                    break
#            elif user_input not in secret_word:
#                if user_input in vowels:
#                    guesses_remaining -= 2
#                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
#                    if guesses_remaining > 0:
#                        print("-------------")
#                        print("You have", guesses_remaining, "guesses left.")
#                        print("Available letters: " + get_available_letters(letters_guessed))
#                    else:
#                        print("-------------")
#                        print("Sorry, you ran out of guesses. The word was", secret_word + ".")
#
#                else:
#                    guesses_remaining -= 1
#                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
#                    if guesses_remaining > 0:
#                        print("-------------")
#                        print("You have", guesses_remaining, "guesses left.")
#                        print("Available letters: " + get_available_letters(letters_guessed))
#                    else:
#                        print("-------------")
#                        print("Sorry, you ran out of guesses. The word was", secret_word + ".")
#
#        elif flag == False:
#            if guesses_remaining > 0 and warnings_remaining > 0:
#                warnings_remaining -= 1
#                print("-------------")
#                print("You have", guesses_remaining, "guesses left.")
#                print("Available letters: " + get_available_letters(letters_guessed))
#
#            elif guesses_remaining > 1 and warnings_remaining <= 0:
#                warnings_remaining -= 1
#                guesses_remaining -= 1
#                print("-------------")
#                print("You have", guesses_remaining, "guesses left.")
#                print("Available letters: " + get_available_letters(letters_guessed))
#
#            else:
#                guesses_remaining == 0
#                print("-------------")
#                print("Sorry, you ran out of guesses. The word was", secret_word + ".")
#                break
#            
#            
##secret_word = 'apple'
#
##
##
##
### When you've completed your hangman function, scroll down to the bottom
### of the file and uncomment the first two lines to test
###(hint: you might want to pick your own
### secret_word while you're doing your own testing)
##
##
### -----------------------------------
##
##
##
#def match_with_gaps(my_word, other_word):
#    '''
#    my_word: string with _ characters, current guess of secret word
#    other_word: string, regular English word
#    returns: boolean, True if all the actual letters of my_word match the 
#        corresponding letters of other_word, or the letter is the special symbol
#        _ , and my_word and other_word are of the same length;
#        False otherwise: 
#    '''
##    # FILL IN YOUR CODE HERE AND DELETE "pass"
##    my_word = get_guessed_word(secret_word, letters_guessed)
#    my_word_strip = my_word.replace(" ", "")
##    print(my_word_strip)
#    i = 0
#    while len(my_word_strip) == len(other_word):
#        while i < len(my_word_strip):
#            if my_word_strip[i] == '_':
#                i += 1
#            elif my_word_strip[i] == other_word[i]:
#                i += 1
#            else:
#                return False
#        return True
#    else:
#        return False
#                
#other_word = 'pine'
#print(match_with_gaps('p_ _ l', other_word))
##print(match_with_gaps(get_guessed_word(secret_word, letters_guessed), other_word))
##
##
##
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
#     FILL IN YOUR CODE HERE AND DELETE "pass"
#    wordlist = load_words()
#    wordlist = ['ana', 'app', 'pear', 'banana', 'apple', 'assle', 'nuttt', 'pleas', 'aenle']
    wordlist_length_match = []
    my_word_strip = my_word.replace(" ", "")
#    print(my_word_strip)
    for item in wordlist:
        if len(item) == len(my_word_strip):
            wordlist_length_match.append(item)
    
    wordlist_copy = wordlist_length_match[:]
            
    for item in wordlist_length_match:
        i = 0
        while i < len(my_word_strip) - 1:
            if my_word_strip[i] == '_':
                i += 1
            elif my_word_strip[i] == item[i]:
                i += 1
            else:
                wordlist_copy.remove(item)
                break
        while i == len(my_word_strip) - 1:
            if my_word_strip[i] == '_':
                break
            elif my_word_strip[i] == item[i]:
                break
            else:
                wordlist_copy.remove(item)
                break
    if len(wordlist_copy) == 0:
        print("No matches found")
    else:
        print("Possible word matches are:")
        print(" ".join(wordlist_copy))
    return wordlist_copy

#my_word = 'a_ _ '
#print(show_possible_matches(my_word))
#        
#
#
#
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    print("Welcome to the game Hangman! \nI am thinking of a word that is", len(secret_word), "letters long. \nYou have 3 warnings left. \n-------------")
    print("You have", guesses_remaining, "guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))
    while guesses_remaining > 0:
        user_input = str.lower(input("Please guess a letter: "))
        flag = warnings(warnings_remaining, user_input, letters_guessed, secret_word)
#        print(flag) ## to check if warning is functioning
        if flag == True:
            letters_guessed.append(user_input)
            if user_input in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed) == False:
                    print("-------------")
                    print("You have", guesses_remaining, "guesses left.")
                    print("Available letters: " + get_available_letters(letters_guessed))
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print("-------------")
                    print("Congratulations, you won! Your total score for this game is:", guesses_remaining*len(set(secret_word)))
                    break
            elif user_input == '*':
               show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            elif user_input not in secret_word:
                if user_input in vowels:
                    guesses_remaining -= 2
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    if guesses_remaining > 0:
                        print("-------------")
                        print("You have", guesses_remaining, "guesses left.")
                        print("Available letters: " + get_available_letters(letters_guessed))
                    else:
                        print("-------------")
                        print("Sorry, you ran out of guesses. The word was", secret_word + ".")

                else:
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    if guesses_remaining > 0:
                        print("-------------")
                        print("You have", guesses_remaining, "guesses left.")
                        print("Available letters: " + get_available_letters(letters_guessed))
                    else:
                        print("-------------")
                        print("Sorry, you ran out of guesses. The word was", secret_word + ".")

        elif flag == False:
            if guesses_remaining > 0 and warnings_remaining > 0:
                warnings_remaining -= 1
                print("-------------")
                print("You have", guesses_remaining, "guesses left.")
                print("Available letters: " + get_available_letters(letters_guessed))

            elif guesses_remaining > 1 and warnings_remaining <= 0:
                warnings_remaining -= 1
                guesses_remaining -= 1
                print("-------------")
                print("You have", guesses_remaining, "guesses left.")
                print("Available letters: " + get_available_letters(letters_guessed))

            else:
                guesses_remaining == 0
                print("-------------")
                print("Sorry, you ran out of guesses. The word was", secret_word + ".")
                break
#
#
#
## When you've completed your hangman_with_hint function, comment the two similar
## lines above that were used to run the hangman function, and then uncomment
## these two lines and run this file to test!
## Hint: You might want to pick your own secret_word while you're testing.
#
#
if __name__ == "__main__":
#    # pass
#
#    # To test part 2, comment out the pass line above and
#    # uncomment the following two lines.
#    
#    secret_word = choose_word(load_words())
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
