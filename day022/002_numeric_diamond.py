# -*- coding: utf-8 -*-
from __future__ import print_function

def run():
    length = int(raw_input('How long do you want the pyramid?: '))

    for i in range(1, length + 1):
        for j in range(length - i):
            print(' ', end=' ')
        
        for j in range(1, i + 1):
            print(j, end=' ')
        
        for j in range(i - 1, 0, -1):
            print(j, end=' ')

        print()

    for i in range(10):
        
        for j in range(i+2):
            print (" ",end=" ")

        for j in range(1,9-i):
            print (j,end=" ")
        
        for j in range(7-i,0,-1):
            print (j,end=" ")
        
        
        
        

        print()
    


if __name__ == '__main__':
    run()