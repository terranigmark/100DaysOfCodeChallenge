# -*- coding: utf-8 -*-

def fibonacci(output, total_items, value_1, value_2):
    # Calculating output with auxiliar variables
    for items in range(total_items - 2):
        output.append(output[value_1] + output[value_2])
        value_1 += 1
        value_2 += 1

def run():
    # Initializing variables and lists
    values = []
    output = [0, 1] # Always starts with 0, 1
    value_1 = 0
    value_2 = 1

    # Welcome and instructions
    print('*** FIBONACCI SEQUENCE ***')
    print('This program calculates the Fibonacci sequence.')
    total_items = int(raw_input('How many numbers do you want to list?: '))
    
    # Calling calculating function
    fibonacci(output, total_items, value_1, value_2)

    # Rsults output
    print('The {} numbers in the Fibonacci sequence are: '.format(total_items - 2))
    print(output)


if __name__ == '__main__':
    run()