#!/usr/bin/python
# -*- coding: utf-8 -*-
import utils
import greedy
import twoopt
import threeopt
import math
from collections import namedtuple

Point = namedtuple("Point", ["idx", 'x', 'y'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm
    if False:
        ofile = open("tsp.in", "w")
        ofile.write(input_data)
        ofile.flush()
    
    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(i - 1, float(parts[0]), float(parts[1])))
                
    utils.lengthCache = [[0.0 for j in range(nodeCount - (i - 1))] for i in range(nodeCount)]
        
    opt, totalDist, tour = greedy.solve(points)
    #opt, totalDist, tour = twoopt.solve(points, tour, totalDist)
    opt, totalDist, tour = threeopt.solve(points, tour, totalDist)
    
    # prepare the solution in the specified output format
    output_data = str(totalDist) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, tour))
    
    if False:
        ofile = open("tsp.out", "w")
        ofile.write(output_data)
        ofile.flush()
    
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'

