# -*- coding: utf-8 -*-

def run():
    # Initializing lists and variables
    words_list = []
    reverse_words_list = []
    # Instructions and data input
    sentence = str(raw_input('Enter a sentence:\n'))
    # Spliting the sentence in a list
    words_list = sentence.split()
    print(words_list)
    # Aux. variable for iterations
    words_list.reverse()
    
    # Results output in the simpliest way
    print(words_list)



if __name__ == '__main__':
    run()