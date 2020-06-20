#!/bin/python3

import numpy as np


def decode(intcode):

    '''Returns the decoded intcode. '''

    pos = 0

    opcode = intcode[pos]

    while opcode != 99:

        if opcode == 1:

            intcode[intcode[pos+3]] = intcode[intcode[pos+1]] + intcode[intcode[pos+2]]

        elif opcode == 2:

            intcode[intcode[pos+3]] = intcode[intcode[pos+1]] * intcode[intcode[pos+2]]                    
        else:
            raise Exception("unknown opcode: something went wrong")

        pos += 4
        opcode = intcode[pos]

    return intcode
        

if __name__ == '__main__':

    # open input file and create list
    with open('input.txt') as f:
        flist = f.read().split(",")    
    program = [int(bar) for bar in flist]

    
    # restore to "1202 program alarm" and decode program
    program[1] = 12
    program[2] = 2
    decoded_program = decode(program)
    
    result = decoded_program[0]

    # write result to output file
    with open("output.txt", "a") as out:
        out.write(str(result))


