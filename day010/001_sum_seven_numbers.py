# -*- coding: utf-8 -*-

def run():
    #declaration of variables
    number_count = 1
    number_input = 0
    sum_of_numbers = 0
    positives = 0
    negatives = 0
    zeros = 0

    print('####SUM SEVEN NUMBERS####')
    print('This program sums 7 numbers in a row. Also, you\'ll know how many of them are positives, negatives or zeros.\n')

    for i in range(7):
        number_input = float(raw_input('Input the element number {}: '.format(number_count)))
        sum_of_numbers += number_input
        number_count += 1
        if number_input == 0:
            zeros += 1
        elif number_input > 0:
            positives += 1
        elif number_input < 0:
            negatives += 1
    
    print('\nTOTAL sum: {}'.format(sum_of_numbers))
    print('TOTAL positives: {}'.format(positives))
    print('TOTAL negatives: {}'.format(negatives))
    print('Total zeros: {}'.format(zeros))


if __name__ == '__main__':
    run()