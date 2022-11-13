# Monkey Typewriter
# Kyle Sanquist
# Version 1.0

# Input a word and the program will randomly print letters
# until it prints the letters of your word or phrase in order
# also tracks the time it takes to print your word
# Based off the famous Infinite Monkey Theorem

LETTERS = ['A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z']

import random
import time
from timeit import default_timer as timer

def main():
    valid_word = ''
    while True:
        word_input = input('WORD: ')
        if(word_input.isalpha()):
            valid_word = word_input
            break

    print('\nThe monkey is typing...\n')
    monkey_typewriter(valid_word.upper())

    

def monkey_typewriter(valid_word):
    start = timer()
    chunk_size = 1000
    chunk_count = 0
    while True:
        chunk = ''
        for i in range(0, chunk_size):
            chunk = chunk + random.choice(LETTERS)
            
        if valid_word in chunk:
            end = timer()
            word_start_index = chunk.index(valid_word)
            word_end_index = word_start_index+(len(valid_word)-1)
            chars_before = len(chunk[:word_start_index])
            found_word_chunk = chunk[:word_start_index] + ' *** ' + valid_word + ' *** ' + chunk[word_end_index+1:]
            break
            
        chunk_count += 1
        
        print(f'[{chunk[:3]} ... {chunk[-3:]}]')
        time.sleep(0.25)

    print(f'\n{found_word_chunk}')
  
    print(f'\nTOTAL CHARACTERS : {(chunk_size*chunk_count)+chars_before}')
    print(f'TIME ELAPSED : {round(end-start, 5)}')
    

if __name__ == '__main__':
    main()
