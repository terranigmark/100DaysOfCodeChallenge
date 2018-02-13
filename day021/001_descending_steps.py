# -*- coding: utf-8 -*-

from __future__ import print_function

def run():
    
    length = int(raw_input('How may steps long you want the stairs?: '))

    for i in range(length + 1):
        print('')
        for j in range(i + 1):
            print(j, end=' ')


if __name__ == '__main__':
    run()