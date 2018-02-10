# -*- coding: utf-8 -*-

def run():
    # Iinitializing an empty list
    list_size = 0
    average = 0
    sum_of_list = 0
    number_list = []

    # Specify the list's size
    list_size = int(raw_input('How many elements will have your list?: '))
    
    # Loop to input values into a list
    for times in range(list_size):
        number_list.append(float(raw_input('Enter the element number {}: '.format(times + 1))))
        sum_of_list += number_list[times]

    # Aux variables
    list_size = len(number_list)
    average = sum_of_list / list_size

    # List output
    print('Your numberes are: {}'.format(number_list))
    print('It has a total of {} elements'.format(list_size))
    print('The total sum of elements is: {}'.format(sum_of_list))
    print('The average in the sum of the list is: {}'.format(average))

if __name__ == '__main__':
    run()