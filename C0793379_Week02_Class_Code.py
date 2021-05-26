print("-------------------Program for calculating area of Circle-----------------------------")

from math import pi


def get_input():
    global radius
    radius = float(input("Enter the radius of the circle : "))


def calculate():
    global area
    area = pi * radius ** 2


def display_area():
    print("The area of the circle  is: " + str(area))


def main():
    get_input()
    calculate()
    display_area()


main()
