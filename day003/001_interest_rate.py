# -*- coding: utf-8 -*-
# This program calculate either the simple or complex interest rate

def simple_interest():
    global capital
    global periods
    global capital_ammount
    global interest_rate
    
    capital = float(raw_input('Enter your capital ammount: '))
    interest_rate = float(raw_input('Enter your interest rate in percentage (%): '))
    periods = int(raw_input('Enter the periods it\'ll be calculated: '))

    capital_ammount = capital + (1 + periods + interest_rate)

def compound_interest():   
    global capital
    global periods
    global capital_ammount
    global interest_rate

    capital = float(raw_input('Enter your capital ammount: '))
    interest_rate = float(raw_input('Enter your interest rate in percentage (%): '))
    periods = int(raw_input('Enter the periods it\'ll be calculated: '))

    capital_ammount = capital + ((1 + interest_rate)**periods)
    
def run():
    print('This program calculates an ammount according to its interest rate')
    print('[1] Simple rate')
    print('[2] Compound rate')
    option = int(raw_input())

    if option == 1:
        simple_interest()
        print('Your capital of {} after {} periods with {} interest rate, generates a total of: {}'.format(capital, periods, interest_rate, capital_ammount))
    elif option == 2:
        compound_interest()
        print('Your capital of {} after {} periods with {} interest rate, generates a total of: {}'.format(capital, periods, interest_rate, capital_ammount))
    else:
        print('INVALID OPTION, TRY AGAIN')


if __name__ == '__main__':
    run()