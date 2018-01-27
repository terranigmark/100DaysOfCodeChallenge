# -*- coding: utf-8 -*-
#This program asks te user for his/her name and age
#Then return the year he/she will be 100 years old

def run():
    #Data input
    name = raw_input('What\'s your name?: ')
    age = int(raw_input('What\'s your age?: '))

    #Result calculation
    older = (2018 - age) + 100

    #Result output
    print('You\'ll be 100 years old in the {} year!'.format(older))


if __name__ == '__main__':
    run()