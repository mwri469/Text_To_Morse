"""
This script aims to use a simple GPIO4 -> led -> ground circuit to
display a sentence in morse code using the led.
Author: Martin Wright
Date: 14 MAY 2022
"""

# Imports
from functions_morse import *

def main():
    # Get input sentence from user
    sentence = input('Enter sentence: ')

    # Remove spaces
    sentence.replace(" ", "")

    # Print letters
    for letter in sentence:        
        try:
            letter_funs[letter.upper()]()
        except KeyError:
            print(letter + " is not available, sorry.")
            break

if __name__ == '__main__':
    main()
