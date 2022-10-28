#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:42:34 2020

@author: pingu
"""
user_input = '*'
letters_guessed = ['a', 'p']
secret_word = 'apple'
warnings_remaining = 3
get_guessed_word = 'app_ _ '

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
                print("Oops! You've already guessed that letter. You now have", warnings_remaining - 1, "warnings left:", get_guessed_word)
                return flag
        elif user_input == '*':
            flag = True
            return flag
        else:
            flag = False
            print("That is not a valid letter. You have", warnings_remaining - 1, "warnings left:", get_guessed_word)
            return flag
    if warnings_remaining == 1:
        if str.isalpha(user_input) == True and len(user_input) == 1:
            if user_input not in letters_guessed:
                flag = True
                return flag
            else:
                flag = False
                print("Oops! You've already guessed that letter. You now have 0 warnings left:", get_guessed_word)
                return flag
        elif user_input == '*':
            flag = True
            return flag
        else:
            flag = False
            print("That is not a valid letter. You have 0 warnings left:", get_guessed_word)
            return flag
    if warnings_remaining <= 0:
        if str.isalpha(user_input) == True and len(user_input) == 1:
            if user_input not in letters_guessed:
                flag = True
                return flag
            else:
                flag = False
                print("Oops! You've already guessed that letter. You now have no warnings left so you lose one guess:", get_guessed_word)
                return flag
        elif  user_input == '*':
            flag = True
            return flag
        else:
            flag = False
            print("That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word)
            return flag
print(warnings(warnings_remaining, user_input, letters_guessed, secret_word))