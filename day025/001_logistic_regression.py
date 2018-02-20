# -*- coding: utf-8 -*-

def run():
    # Initialization of variables
    weigths = []
    x1_array = []
    x2_array = []
    output = []
    option = False

    while option == False:
        choice = int(raw_input(
            '''
            [1] AND
            [2] OR
            [3] NAND
            [4] NOR
            [5] XOR
            [6] XNOR

            Choose a Logic Gate option:
            '''))
        
        if choice < 1 or choice > 6:
            choice = int(raw_input('Invalid option, choice another: '))
        elif choice == 1:
            print('You choosed the logic gate AND')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            option = True
        elif choice == 2:
            print('You choosed the logic gate OR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            option = True
        elif choice == 3:
            print('You choosed the logic gate NAND')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            option = True
        elif choice == 4:
            print('You choosed the logic gate NOR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            option = True
        elif choice == 5:
            print('You choosed the logic gate XOR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            option = True
        elif choice == 6:
            print('You choosed the logic gate XNOR')
            x1_array = [0, 0, 1, 1]
            x2_array = [0, 1, 0, 1]
            option = True

    for values in range(3):
        if values == 0:
            weigths.append(float(raw_input('Enter the value for the bias: ')))
        else:
            weigths.append(float(raw_input('Enter the value for X{}: '.format(values))))
    
    print(
        '''
        You arrays are: 
        Weights: {}
        X1: {}
        X2: {}
        '''.format(weigths, x1_array, x2_array))

    

if __name__ == '__main__':
    run()