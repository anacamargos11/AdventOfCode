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


    # COMPUTE THE AMOUNT OF FUEL REQUIRED (result)
    #-----------------------------------------------------------------
    
    result = 0  

    # fuel of all modules
    fuel_modules = fuel(np.array(modules))     
    sum_fuel_modules = np.sum(fuel_modules, where = fuel_modules>0)

    while sum_fuel_modules > 0:

        # keep going while fuel_modules has at least one positive element
        result += sum_fuel_modules  

        # compute fuel of fuel for all modules
        fuel_modules = fuel(fuel_modules)
        sum_fuel_modules = np.sum(fuel_modules, where = fuel_modules>0)
         
    #------------------------------------------------------------------


    # write result to output file
    with open("output.txt", "a") as out:
        out.write(str(result))


