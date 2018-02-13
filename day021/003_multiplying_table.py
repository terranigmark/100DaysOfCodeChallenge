# -*- coding: utf-8 -*-

from __future__ import print_function

def run():
    length = int(raw_input('How may steps long you want the stairs?: '))

    for j in range(1, length):
        print(' ')
        for i in range(1, length):
            k = i * j
            if k > 10:
                print(k, end=' ')
            else:
                print(k, end='  ')


if __name__ == '__main__':
    run()