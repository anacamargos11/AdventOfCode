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
    original_program = [int(bar) for bar in flist]

    program = original_program.copy()
    output = 19690720
  
    # try different noun and verb combinations 
    is_looping = True
    for noun in range(0,100):    
        for verb in range(0,100):
            program[1] = noun
            program[2] = verb
            decoded_program = decode(program)

            if decoded_program[0] == output:
                is_looping = False
                break
          
            else:
                program = original_program.copy()

        if not is_looping:
            break

    result = 100 * noun + verb

    # write result to output file
    with open("output.txt", "a") as out:
        out.write(str(result))


