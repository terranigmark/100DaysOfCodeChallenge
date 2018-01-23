# -*- coding: utf-8 -*-

def main():
    #This program calculates the area of a trapezoid
    #Data input
    print("Please enter the data as required.")
    heigth = float(raw_input("Enter the height of the trapezoid: "))
    bottom_length = float(raw_input("Enter the length of the bottom base: "))
    top_length = float(raw_input("Enter the length of the top base: "))

    #Data calculation
    area = 1/2 * (bottom_length + top_length) * heigth

    #Data output
    print("The area is: ", area)
    

if __name__ == '__main__':
    main()