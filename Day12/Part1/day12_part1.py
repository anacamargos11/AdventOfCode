#!/bin/python3

import numpy as np
import itertools
import re


class Moon:

    def __init__(self,position):
        self.position = position
        self.velocity = np.zeros(3)

    def get_energy(self):
        pot = np.sum(np.abs(self.position))
        kin = np.sum(np.abs(self.velocity))
        return pot * kin
       
    @classmethod
    def accelerate(cls,*moon):

        for coord in range(0,3):

            for (i,j) in itertools.combinations([0,1,2,3],2):

                if moon[i].position[coord] > moon[j].position[coord]:
                    moon[i].velocity[coord] -= 1
                    moon[j].velocity[coord] += 1

                elif moon[i].position[coord] < moon[j].position[coord]:
                    moon[i].velocity[coord] += 1
                    moon[j].velocity[coord] -= 1

    @classmethod
    def walk(cls,*moon):

        for i in range(0,3):

            moon[0].position[i] += moon[0].velocity[i]
            moon[1].position[i] += moon[1].velocity[i]
            moon[2].position[i] += moon[2].velocity[i]
            moon[3].position[i] += moon[3].velocity[i]



if __name__ == '__main__':

    # open input file and create a positions list
    # example of positions list: ([-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1])

    with open('input.txt') as f:
        flist = f.read().splitlines()

    positions = []
    for item in flist:
        positions.append(list(map(int, re.sub(r'[xyz]|=|<|>','',item).split(","))))

    # creating moon objects with their positions    
    Io     = Moon(np.array(positions[0]))
    Europa = Moon(np.array(positions[1]))
    Ganymede = Moon(np.array(positions[2]))
    Callisto = Moon(np.array(positions[3]))

    # simulating the system for 1000 time steps
    for t in range(0,1000):
        Moon.accelerate(Io,Europa,Ganymede,Callisto)
        Moon.walk(Io,Europa,Ganymede,Callisto)

    energy = [m.get_energy() for m in [Io,Europa,Ganymede,Callisto] ]
    total_energy = sum(energy)


    #write result to output file
    with open("output.txt", "a") as out:
        out.write(str(total_energy))


