# -*- coding: utf-8 -*-

def process_results(total_items, items, list_ends):
    # Input process
    for times in range(total_items):
        items.append(int(raw_input('Enter the element no. {}: '.format(times + 1))))

    # Take ends into a new list
    # - First element
    list_ends.append(items[0])
    
    # - Second element
    second_item_index = len(items) - 1
    list_ends.append(items[second_item_index])

def run():
    # Initialize lists
    items = []
    list_ends = []

    # Description
    print('*** LIST ENDS ***')
    print('This program will give the first and last value from a list given by the user.\n')

    # Instructions
    total_items = int(raw_input('Enter how many number you will give: '))
    
    process_results(total_items, items, list_ends)

    # Result output
    print('The results are: {}'.format(list_ends))


if __name__ == '__main__':
    run()