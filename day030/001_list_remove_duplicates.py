# -*- coding: utf-8 -*-
import random

def generating_list(data_amount, numbers_list, upper_limit):
    # Adding elements to a list
    for times in range(data_amount):
        numbers_list.append(random.randrange(0, upper_limit))

def generating_set(data_amount, numbers_set, numbers_list):
    # Adding elements from a list to a set
    for times in range(data_amount):
        numbers_set.add(numbers_list[times])

def run():
    # Initializing list and set
    numbers_list = []
    numbers_set = set()

    # Instructions
    data_amount = int(raw_input('Select how big you want the data set: '))
    upper_limit = int(raw_input('Input the upper limit of the range which starts from zero: '))
    print('Your data set will have {} elements and the range goes from 0 to {}'.format(data_amount, upper_limit))

    # Processing data
    generating_list(data_amount, upper_limit)
    generating_set(data_amount, numbers_list)

    # Results output
    print('This is the list of numbers randomly generated:')
    print(numbers_list)
    print('')
    print('This is the list of non-repeated numbers randomly generated:')
    print(numbers_set)

if __name__ == '__main__':
    run()