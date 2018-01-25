# -*- coding: utf-8 -*-
#This program allows you to know the IRR of a determined capital

def run():
    print('****NET PRESENT VALUE**** ')
    print('Please enter the data as resquested.')
    
    #Data input
    initial_investment = float(raw_input('Initial Investment: $'))
    periods = int(raw_input('Number of periods: '))
    internal_rate_of_return = float(raw_input('Internal Rate of Return (%): '))
    internal_rate_of_return = internal_rate_of_return / 100
    cash_flow_period = []

    #Cash flows input
    for number_of_periods in range(0, periods):
        new_cash_flow = float(raw_input('Cash flow for the period number {}: '.format(number_of_periods+1)))
        cash_flow_period.append(new_cash_flow)

    #Reverse list to proper order
    cash_flow_period.reverse()

    #Result calculation
    number_of_periods = 0
    net_present_value = (initial_investment * -1)

    for number_of_periods in range (0, periods):
        net_present_value += (cash_flow_period[number_of_periods])/((1 + internal_rate_of_return) ** number_of_periods + 1)

    print(net_present_value)


if __name__ == '__main__':
    run()