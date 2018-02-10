# -*- coding: utf-8 -*-
from __future__ import print_function

def run():
    # Inputs for size
    width = int(raw_input('Enter the width of the net: '))
    height = int(raw_input('Enter the height of the net: '))

    for j in range(height):
        print('')
        for i in range(width):
            print('*', end=' ')    

if __name__ == '__main__':
    run()