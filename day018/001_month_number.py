# -*- coding: utf-8 -*-

def run():
    # Variable declaration
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    done = False

    # Starting the main loop
    while done == False:

        # Ask the user for a numeric input of a number
        month_number = int(raw_input('Enter the number of a month to show it\'s abreviation: '))

        # Validating cases:
        if month_number < 1 or month_number > 13:
            print('\nInvalid number, try within the range of 1 and 12')
            month_number = int(raw_input('Enter the number of a month to show it\'s abreviation: '))
        elif month_number == 1:
            print'The month number {} is: '.format(month_number), months[0:3]
        elif month_number == 2:
            print'The month number {} is: '.format(month_number), months[3:6]
        elif month_number == 3:
            print'The month number {} is: '.format(month_number), months[6:9]
        elif month_number == 4:
            print'The month number {} is: '.format(month_number), months[9:12]
        elif month_number == 5:
            print'The month number {} is: '.format(month_number), months[12:15]
        elif month_number == 6:
            print'The month number {} is: '.format(month_number), months[15:18]
        elif month_number == 7:
            print'The month number {} is: '.format(month_number), months[18:21]
        elif month_number == 8:
            print'The month number {} is: '.format(month_number), months[21:24]
        elif month_number == 9:
            print'The month number {} is: '.format(month_number), months[24:27]
        elif month_number == 10:
            print'The month number {} is: '.format(month_number), months[27:30]
        elif month_number == 11:
            print'The month number {} is: '.format(month_number), months[30:33]
        elif month_number == 12:
            print'The month number {} is: '.format(month_number), months[33:36]

        # Asking the user to quit the program
        option = str(raw_input('Do you want to quit? [Y/N]: ')).lower()

        if option.lower() == 'y':
            done == True
            print('Thanks for using our software!')
            break
        else:
            continue

        


if __name__ == '__main__':
    run()