# -*- coding: utf-8 -*-
#This program allows you to know the IRR of a determined capital

def run():
    print('****NET PRESENT VALUE**** ')
    print('Please enter the data as resquested.\n')
    
    #Data input
    initial_investment = float(raw_input('Initial Investment: $'))
    periods = int(raw_input('Number of periods: '))
    internal_rate_of_return = float(raw_input('Internal Rate of Return (%): '))
    internal_rate_of_return = internal_rate_of_return / 100
    cash_flow_period = []

    #Cash flows input
    for number_of_periods in range(0, periods):
        new_cash_flow = float(raw_input('Cash flow for the period number {}: '.format(number_of_periods+1)))
        cash_flow_period.append(float(new_cash_flow))

    #Result calculation
    number_of_periods = 0
    net_present_value = 0

    for number_of_periods in range (0, periods):
        net_present_value += cash_flow_period[number_of_periods] / ((1 + internal_rate_of_return) ** (number_of_periods + 1))

    net_present_value -= initial_investment

    if net_present_value > 0:
        viability = 'VIABLE'
    else:
        viability = 'NOT VIABLE'

    print('')
    print('Your Net Present Value is: ${}'.format(net_present_value))
    print('Conclusion: your project is {}'.format(viability))



if __name__ == '__main__':
    run()