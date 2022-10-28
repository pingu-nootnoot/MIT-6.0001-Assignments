#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:31:47 2020

@author: pingu
"""
#word = 'appl*'
#VOWELS = 'aeiou'
#word_list = ['ear', 'name', 'random', 'idk', 'apple']
#word_list = ['ear', 'name', 'random', 'idk']
#word_list = ['ear', 'name', 'random', 'idk', 'appll']
#
#
#flag = False
#i = 0
#word_copy = ''
#while i < len(word):
#    word_copy = word.replace('*', VOWELS[i])
#    if word_copy in word_list:
#        flag = True
#        break
#    else:
#        i += 1
#print(flag)



#word = 'appl*'
#hand = {'a': 1, '*': 1, 'p': 2, 'l': 1, 'e': 1}
#hand = {'a': 1, '*': 1, 'p': 2, 'l': 1}
#hand = {'e': 1, '*': 1, 'p': 2}
#
#word_dict = {}
#for letter in word:
#    if letter not in word_dict.keys():
#        word_dict[letter] = 1
#    elif letter in word_dict.keys():
#        word_dict[letter] += 1
#print(word_dict)
#
#valid = False
#for key, value in word_dict.items():
#    if key in hand:
#        if word_dict[key] == hand[key]:
#            valid = True
#        else:
#            valid = False
#            break
#    else:
#        valid = False
#print(valid)
#VOWELS = 'aeiou'
#word = 'appl*'
#hand = {'a': 1, '*': 1, 'p': 2, 'l': 1, 'e': 1}
#word_list = ['ear', 'name', 'random', 'idk', 'apple']

#hand_len = 0
#for letter in hand.keys():
#    hand_len += hand[letter] 
#print(hand_len)
import random

hand = {'*': 1, 'o': 1, 'i': 1, 't': 1, 'j': 1, 'c': 1, 'b': 1}
letter = '*'

alphabet = 'abcdefghijklmnopqrstuvwxyz*'
avai_letters = list(alphabet)
if letter == '*':
    hand = hand
else:
    for i in hand.keys():
        avai_letters.remove(i)
    if letter in hand.keys(): 
        x = random.choice(avai_letters)
        hand[x] = hand.pop(letter)
print(hand)














