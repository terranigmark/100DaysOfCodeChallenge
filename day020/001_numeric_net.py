# -*- coding: utf-8 -*-
from __future__ import print_function

def run():
    # Inputs for size
    length = int(raw_input('Enter the length of the net: '))
    times = int(raw_input('Enter how many lines you want: '))

    for j in range(times):
        print('')
        for i in range(length + 1):
            print(i, end=' ')

if __name__ == '__main__':
    run()