# -*- coding: utf-8 -*-
import random

def run():
    #Creating lists and adding values
    series_1 = []
    series_2 = []
    common_numbers = []

    for x in range(0,30):
        series_1.append(random.randint(0,100))
        series_2.append(random.randint(0,100))
    
    for i in range(0, 30):
        if series_2[i] in series_1:
            common_numbers.append(series_2[i])
    
    print('First series of numbers: ')
    print(series_1)
    print('\nSecond series of numbers: ')
    print(series_2)
    print('\nCommon numbers: ')
    print(common_numbers)
            




if __name__ == '__main__':
    run()