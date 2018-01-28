# -*- coding: utf-8 -*-

def run():
    reverse_word = []
    word = []
    input = raw_input('Enter a word to know if its a palindrome or not: ')
    word = str(input)
    reverse_word = word[::-1]

    if word == reverse_word:
        print('The word {} is a palindrome!'.format(word))
    else:
        print('The word {} is NOT a palindrome'.format(word))

if __name__ == '__main__':
    run()