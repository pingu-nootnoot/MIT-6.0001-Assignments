#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:28:05 2020

@author: pingu
"""
secret_word = 'apple'
letters_guessed = ['a', 'p']
get_guessed_word = 'app_ _ '
is_word_guessed = False
get_available_letters = 'bcdefghijklmnoqrstuvwxyz'
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
        else:
            flag = False
            print("That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            return flag
        
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
    wordlist = ['ana', 'app', 'pear', 'banana', 'apple', 'assle', 'nuttt', 'pleas', 'aenle']
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
        print(wordlist_copy)
    return wordlist_copy

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
    print("Available letters: " + get_available_letters)
    while guesses_remaining > 0:
        user_input = str.lower(input("Please guess a letter: "))
        flag = warnings(warnings_remaining, user_input, letters_guessed, secret_word)
        if flag == True:
            letters_guessed.append(user_input)
            if user_input in secret_word:
                print("Good guess:", get_guessed_word)
                if is_word_guessed == False:
                    print("-------------")
                    print("You have", guesses_remaining, "guesses left.")
                    print("Available letters: " + get_available_letters)
                if is_word_guessed == True:
                    print("-------------")
                    print("Congratulations, you won! Your total score for this game is:", guesses_remaining*len(set(secret_word)))
                    break
            elif user_input == '*':
               show_possible_matches(get_guessed_word)
            elif user_input not in secret_word:
                if user_input in vowels:
                    guesses_remaining -= 2
                    print("Oops! That letter is not in my word:", get_guessed_word)
                    if guesses_remaining > 0:
                        print("-------------")
                        print("You have", guesses_remaining, "guesses left.")
                        print("Available letters: " + get_available_letters)
                    else:
                        print("-------------")
                        print("Sorry, you ran out of guesses. The word was", secret_word + ".")

                else:
                    guesses_remaining -= 1
                    print("Oops! That letter is not in my word:", get_guessed_word)
                    if guesses_remaining > 0:
                        print("-------------")
                        print("You have", guesses_remaining, "guesses left.")
                        print("Available letters: " + get_available_letters)
                    else:
                        print("-------------")
                        print("Sorry, you ran out of guesses. The word was", secret_word + ".")

        elif flag == False:
            if guesses_remaining > 0 and warnings_remaining > 0:
                warnings_remaining -= 1
                print("-------------")
                print("You have", guesses_remaining, "guesses left.")
                print("Available letters: " + get_available_letters)

            elif guesses_remaining > 1 and warnings_remaining <= 0:
                warnings_remaining -= 1
                guesses_remaining -= 1
                print("-------------")
                print("You have", guesses_remaining, "guesses left.")
                print("Available letters: " + get_available_letters)

            else:
                guesses_remaining == 0
                print("-------------")
                print("Sorry, you ran out of guesses. The word was", secret_word + ".")
                break