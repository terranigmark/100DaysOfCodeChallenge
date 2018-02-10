# -*- coding: utf-8 -*-
from __future__ import print_function

def run():
    # Ask the user for how many asterisks to show
    amount = int(raw_input('How many stars you want to see?: '))
    
    # Code that print asteriks in a row
    for i in range(amount):
        print('*', end=' ')

if __name__ == '__main__':
    run()