# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('C U R R E N C I E S   C A L C U L A T O R')
    print('This program converts Mexican pesos to Colombian pesos')
    print('')

    ammount = float(raw_input('Input the ammount of Mexican pesos to convert into Colombian pesos: '))

    result = foreign_exchange_calculator(ammount)

    print('${} Mexican pesos are  ${} Colombian pesos'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()