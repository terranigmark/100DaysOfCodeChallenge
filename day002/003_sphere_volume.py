# -*- coding: utf-8 -*-
#This program calculate the volme of a sphere

def run():
    pi = 3.1415

    #Data input
    print('Sphere volume')
    radius = float(raw_input('Enter the radius length: '))

    #Result calculation
    volume = ((4 * pi) * (radius**3)) / 3

    #Result output
    print('The sphere volume is: {}'.format(volume))

if __name__ == '__main__':
    run()