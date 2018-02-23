# -*- coding: utf-8 -*-

def run():
    # Initialization of variables
    weigths = []
    x1_array = []
    x2_array = []
    expected_output = []
    output = []
    difference_counter = 0
    option = False

    # Loop to input a valid option
    while option == False:
        choice = int(raw_input(
            '''
            [1] AND
            [2] OR
            [3] NAND
            [4] NOR
            [5] XOR
            [6] XNOR

            Choose a Logic Gate option: '''))

        print('')
        
        # Valid cases for the options
        # -- Expected outputs belongs to their own logic gate
        if choice == 1:
            print('You choosed the logic gate AND')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            expected_output = [0, 0, 0, 1]
            option = True
        elif choice == 2:
            print('You choosed the logic gate OR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            expected_output = [0, 1, 1, 1]
            option = True
        elif choice == 3:
            print('You choosed the logic gate NAND')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            expected_output = [1, 1, 1, 0]
            option = True
        elif choice == 4:
            print('You choosed the logic gate NOR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            expected_output = [1, 0, 0, 0]
            option = True
        elif choice == 5:
            print('You choosed the logic gate XOR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            expected_output = [0, 1, 1, 0]
            option = True
        elif choice == 6:
            print('You choosed the logic gate XNOR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            expected_output = [1, 0, 0, 1]
            option = True
        else:
            print('Invalid option, choice another: ')

    # Input for the bias, X1 and X2 values
    for values in range(3):
        if values == 0:
            weigths.append(float(raw_input('Enter the value for the bias: ')))
        else:
            weigths.append(float(raw_input('Enter the value for X{}: '.format(values))))
    
    # Showing the inputs by the user
    print(
        '''
        You arrays are: 
        Weights: {}
        X1: {}
        X2: {}
        '''.format(weigths, x1_array, x2_array))
    
    # Calculating the output values
    for times in range(4):
        element = ((x1_array[times] * weigths[1]) + (x2_array[times] * weigths[2]) + weigths[0])
        if element < 0:
            output.append(0)
        else:
            output.append(1)
    
    # Checking difference between the output and expected output values
    for times in range(4):
        if expected_output[times] != output[times]:
            difference_counter += 1
    
    # Resolving type of result
    if difference_counter == 0:
        result = 'TAUTOLOGY'
    elif difference_counter == 1:
        result = 'CONTINGENCY'
    else:
        result = 'CONTRADICTION'

    # Results output
    print('Expected output is: {}'.format(expected_output))
    print('The output values are: {}'.format(output))
    print('Then the result is a {}'.format(result))
    
if __name__ == '__main__':
    run()