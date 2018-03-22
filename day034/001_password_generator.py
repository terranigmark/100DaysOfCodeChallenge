# -*- coding: utf-8 -*-
# Importing libraries
from __future__ import print_function
import random

def generate_new_pass(new_password, password_list, password_reference, pass_index):
    password_reference.append(str(raw_input('What\'s your password reference?: ')))
    pass_length = int(raw_input('Choose the character length of your password: ')) #Defines password strength
    # Generates random characters for the new password
    for i in range(0, pass_length):
        new_password.append(chr(random.randrange(32,126)))
        
    # Stores the password in a list
    password = ''.join(new_password)
    password_list.append(password)

    # Data output
    print('Password #{}: {} \nReference: {} '.format(pass_index + 1, password_list[pass_index], password_reference[pass_index]))

    # Clearing the list used to create the password
    for i in range(0, pass_length):
        new_password.pop()

def view_stored_passwords(pass_index, password_list, password_reference):
    print(pass_index)
    for i in range(0, pass_index):
        print('Password #{}: {}'.format(i + 1, password_list[i]))
        print('Reference: {}\n'.format(password_reference[i]))

def view_specific_password(list_index, password_list, password_reference):
    list_index = int(raw_input('Select an index to view its password: '))
    print('Password #{}: {}'.format(list_index, password_list[list_index - 1]))
    print('Reference: {}\n'.format(password_reference[list_index - 1]))

def delete_password(password_list, password_reference, list_index):
    view_specific_password(list_index, password_list, password_reference)
    delete_confirmation = str(raw_input('Do you want to delete this password? [Y/N]\n'))
    print(list_index)

    if delete_confirmation.lower() == 'y':
        password_list.pop(list_index)
        password_reference.pop(list_index)
    elif delete_confirmation.lower() == 'n':
        print('Password #{} was not deleted'.format(list_index + 1))
    


def run():
    # Initializing variables
    pass_length = 0
    done = False
    option = 0
    new_password = []
    password_reference = []
    password_list = []
    password = ''
    list_index = 0
    pass_index = 0

    # Welcome and instructions:
    print('P A S S W O R D   G E N E R A T O R')

    while done == False:
        option = int(raw_input(
            '''
            Choose an option

            [1] Create a new password
            [2] View stored passwords
            [3] View specific password
            [4] Delete a password
            [5] Change a current password
            [6] EXIT
            
            '''))

        if option == 5:
            done = True
        elif option == 1:
            generate_new_pass(new_password, password_list, password_reference, pass_index)
            pass_index = len(password_list)
        elif option == 2:
            view_stored_passwords(pass_index, password_list, password_reference)
        elif option == 3:
            view_specific_password(list_index, password_list, password_reference)
        elif option == 4:
            delete_password(password_list, password_reference, list_index)
            pass_index = len(password_list)
        else:
            print('\nChoose a valid option!')            

    else:
        print('\nGOOD BYE!')


if __name__ == '__main__':
    run()