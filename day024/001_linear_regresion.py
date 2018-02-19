# -*- coding: utf-8 -*-

def run():
    # List creation for data storage and variables
    x_values = []
    y_values = []
    summation_of_y_times_n = 0
    sum_of_y_values = 0
    summation_of_n = 0
    summation_of_n_pow_2 = 0
    summation_of_n_powered_by_2 = 0
    slope = 0
    average_of_y = 0
    average_of_x = 0
    intersection_point = 0
    forecast = 0

    unit_modifier = 1
    
    
    # Data input
    print('LINEAR REGRESION CALCULATOR')
    print('')
    data_rows = int(raw_input('Enter the ammount of values you will use: '))
    forecast_value_to_predict = float(raw_input('Enter the value for X to predict: '))
    print('Ok, you wil work with {} data'.format(data_rows))
    print('')

    for times in range(data_rows):
        x_values.append(float(raw_input('Enter the value #{} in X : '.format(times + 1))))
        y_values.append(float(raw_input('Enter the value #{} in Y: '.format(times + 1))))

    # Displaying inputs
    print('')
    print('Values in X:')
    print(x_values)
    print('Values in Y:')
    print(y_values)
    print('')

    # Slope calculation
    # --Sum of y times n
    for times in range(data_rows):
        summation_of_y_times_n += (y_values[times] * (times + 1))

    # -- Sum of Y values
    for times in range(data_rows):
        sum_of_y_values += y_values[times]

    # --Summmation of n
    for times in range(data_rows):
        summation_of_n += times + 1

    # -- Summation of n^2 for each period
    for times in range(data_rows):
        summation_of_n_pow_2 += (times + 1) ** 2

    # -- Summation of n^2
    for times in range(data_rows):
        summation_of_n_powered_by_2 = summation_of_n ** 2

    # -- Slope resultant
    slope = ((data_rows * (summation_of_y_times_n)) - ((sum_of_y_values) * (summation_of_n))) / ((data_rows * (summation_of_n_pow_2)) - (summation_of_n_powered_by_2))

    # Intersection point calculation
    # -- Average of Y values
    average_of_y = sum_of_y_values / data_rows
    print(average_of_y)

    # -- Average of X values
    data_rows = float(data_rows)
    average_of_x = summation_of_n / data_rows * 1.0
    print(average_of_x)

    # -- Intersection result
    intersection_point = average_of_y - (slope * average_of_x)

    # Forecast calculation
    forecast = intersection_point + ((slope) * (forecast_value_to_predict))

    print('Slope: {}'.format(slope))
    print('Intersection point: {}'.format(intersection_point))
    print('Forecast for {} as next value: {}'.format(forecast_value_to_predict, forecast))

if __name__ == '__main__':
    run()