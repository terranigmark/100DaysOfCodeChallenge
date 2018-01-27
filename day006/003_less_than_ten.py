# -*- coding: utf-8 -*-

def run():
    #Initializing and printing list
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = []
    print(a)

    #Data input
    check = int(raw_input('Choose a number and all the number lesser than it will be shown: '))

    #Result calculation
    for i in range(0, 10):
        if a[i] < check:
            result.append(a[i])
             
    print(result)

if __name__ == '__main__':
    run()