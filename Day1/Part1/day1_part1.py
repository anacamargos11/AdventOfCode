#!/bin/python3

import numpy as np


def fuel(mass):

    '''Returns the necessary fuel to launch a module. '''

    fuel = np.floor(mass/3) - 2

    return fuel
        

if __name__ == '__main__':

    # open input file and create list
    with open('input.txt') as f:
        flist = f.read().splitlines()    
    modules = [int(bar) for bar in flist]

    # compute the amount of fuel required (result)   
    total_fuel = fuel(np.array(modules))
    result = np.sum(total_fuel)

    # write result to output file
    with open("output.txt", "a") as out:
        out.write(str(result))


