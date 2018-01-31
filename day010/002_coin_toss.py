# -*- coding: utf-8 -*-
import random

def run():
    #variable declaration
    times_tossed = 0
    random_selector = 0
    heads = 0
    tails = 0

    print('*****COIN TOSS SIMULATOR*****')
    print('Choose how many times you want to flip the coin to know the results!')

    times_tossed = int(raw_input('Enter how many times the coin will be tossed: '))

    for times in range(times_tossed):
        random_selector = random.randrange(0,2)

        if random_selector == 0:
            print('Heads')
            heads += 1
        elif random_selector == 1:
            print('Tails')
            tails += 1
    
    print('')
    print('The coin was tossed {} times'.format(times_tossed))
    print('TOTAL heads: {}'.format(heads))
    print('Total tails: {}'.format(tails))

if __name__ == '__main__':
    run()