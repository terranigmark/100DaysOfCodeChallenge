# -*- coding: utf-8 -*-
from __future__ import print_function

def run():

    length = int(raw_input('Choose how long you want the stairs: '))

    for j in range(length):
        print('')
        for i in range(length):
            print(j, end=' ')
        length -= 1
if __name__ == '__main__':
    run()