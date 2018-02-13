# -*- coding: utf-8 -*-

from __future__ import print_function

def run():

    i = 0
    length = int(raw_input('How may steps long you want the stairs?: '))
    
    for row in range(length):
      
        for j in range(row):
            print(' ', end=' ')

        for j in range(length - row):
            print(j, end=' ')

        print(' ')

if __name__ == '__main__':
    run()