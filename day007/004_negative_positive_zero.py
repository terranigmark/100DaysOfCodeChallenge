# -*- coding: utf-8 -*-

def run():
    number = float(raw_input('Enter a number to read its value: '))

    if number > 0:
        print('Your number is POSITIVE')
    elif number < 0:
        print('Ypur number is NEGATIVE')
    else:
        print('Your number is ZERO')


if __name__ == '__main__':
    run()