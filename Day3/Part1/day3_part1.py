#!/bin/python3

import numpy as np
import itertools


def walk(direction):

    '''Updates the position increment according to the directions. '''

    increment = int(direction[1:])

    update = np.zeros(2)

    if direction[0] == 'R':

        update[0] += increment

    elif direction[0] == 'L':

        update[0] -= increment

    elif direction[0] == 'U':

        update[1] += increment

    elif direction[0] == 'D':

        update[1] -= increment

    else:
        raise Exception("Invalid direction paremeter")

    return update
        


def wire_path(pos1, pos2):

    '''Computes the entire path of the wires according to their trajectory. '''

    distance = pos2-pos1

    path = []

    if distance[0] == 0:

        if pos1[1] < pos2[1]:

            for i in range(int(pos1[1]),int(pos2[1])):

                path.append((pos1[0],i))

        elif pos1[1] > pos2[1]:

            for i in range(int(pos2[1]),int(pos1[1])):

                path.append((pos1[0], pos1[1] + pos2[1] - i))


    elif distance[1] == 0:

        if pos1[0] < pos2[0]:

            for i in range(int(pos1[0]),int(pos2[0])):

                path.append((i,pos1[1]))

        elif pos1[0] > pos2[0]:

            for i in range(int(pos2[0]),int(pos1[0])):

                path.append((pos1[0] + pos2[0] - i, pos1[1]))

    return path



if __name__ == '__main__':

    # open input file and create list
    with open('input.txt') as f:
        flist = f.read().splitlines()
    wire1_list = flist[0].split(",")    
    wire2_list = flist[1].split(",") 
    

    # initializing empty variables
    p1 = np.zeros(2)                  # position of wire 1
    p2 = np.zeros(2)                  # position of wire 2
    path1 = []                        # total path of wire 1
    path2 = []                        # total path of wire 2
    inter = []                        # list of intersections


    # computing intersections
    for (d1, d2) in zip(wire1_list,wire2_list):

        [path1.append(i) for i in wire_path(p1,p1+walk(d1))]
        [path2.append(i) for i in wire_path(p2,p2+walk(d2))]

        p1 += walk(d1)
        p2 += walk(d2)

    inter = list(set(path1) & set(path2))

    dist = [abs(x) + abs(y) for (x,y) in inter]

    result = sorted(dist)[1]


    #write result to output file
    with open("output.txt", "a") as out:
        out.write(str(result))


