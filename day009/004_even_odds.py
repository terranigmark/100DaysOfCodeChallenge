# -*- coding: utf-8 -*-

def run():

    limit = int(raw_input('Choose the number list ceiling: '))
    option = str(raw_input('Chose an ODD or EVEN sequence: '))

    while option.lower() != 'odd' and option.lower() != 'even':
        print('Invalid option, try again')
        option = str(raw_input('\nChose an ODD or EVEN sequence: '))
    else:
        if option.lower() == 'even':
            for i in range(0, limit + 2, 2):
                print(i)
        elif option.lower() == 'odd':
            for i in range(0, limit, 3):
                if i == 0:
                    print('1')
                else:
                    print(i)
                    

if __name__ == '__main__':
    run()