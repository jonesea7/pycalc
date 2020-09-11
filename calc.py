#!/usr/bin/env python

# Copyright 2016 -- Levi Starrett & Jay Hankins
# for educational purposes only
#
# For use in CS 190: https://github.com/Purdue-CSUSB/CS-190-F2016/
#
# Calculator -- a four function calculator commandline tool

import sys
import math

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# a -- addend
# b -- augend
def add(a, b):
    return a + b

# Subtract function
# a -- minuend
# b -- subtrahend
def sub(a, b):
    return a - b

# Multiply function
# a -- multiplicand
# b -- multiplier
def mult(a, b):
    return a * b

# Divide function
# a -- dividend
# b -- divisor
def div(a, b):
    return a / b

#Exponent function
def exponentFunction(a, b):
    return a**b


# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while (True):
    print("Welcome to the calculator: +, -, /, *, ^ are your operators have fun.")
    # get input values
    a = input("Enter the first argument: ")
    op = input("Enter the operation: ")
    b = input("Enter the second argument: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number argument...")
        op = None

    # decide function
    if (op != None):
        if (op == "+"):
            print("Sum: ", add(a, b))
        elif (op == "-"):
            print("Difference: ", sub(a, b))
        elif (op == "*"):
            print("Product: ", mult(a, b))
        elif (op == "/"):
            print("Quotient: ", div(a, b))
        elif (op == "^"):
            print("Exponent: ", exponentFunction(a,b))
        else:
            print("Invalid operation...")
    
    """ elif questionUser = input("Do you want the square root of this number? [y/n]")
        if (questionUser == 'y' or question == 'Y')
            squareRootArgument  = input("Enter the number you want the square root of: ")
            print(math.sqrt(squareRootArgument)) """ 
    elif q = input("Quit? [y/n] "):
        if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #

