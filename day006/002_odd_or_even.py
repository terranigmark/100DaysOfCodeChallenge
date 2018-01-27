# -*- coding: utf-8 -*-

def run():
    print('This program check is validates if 2 numbers are odd or even and also if the first one divides evenly the second one.')

    #Data input
    num = int(raw_input('Enter a number to check: '))
    check = int(raw_input('Enter a number to divde by: '))

    #Result calculation
    result = check % num
    if result == 0:
        print('{} divides EVENLY {}!'.format(num, check))
    else:
        print('{} divides ODDLY {}!'.format(num, check))


if __name__ == '__main__':
    run()