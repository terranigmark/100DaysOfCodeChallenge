# -*- coding: utf-8 -*-

def run():
    # Iinitializing an empty list
    number_list = []
    
    # Loop to input values into a list
    for times in range(4):
        number_list.append(float(raw_input('Enter a number: ')))

    # Result output
    print('Your numberes are: {}'.format(number_list))

if __name__ == '__main__':
    run()