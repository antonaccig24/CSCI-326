## nn.py
## Giorgio Antonacci

import functools
import math
import os
import os.path
import shutil

def do(filename):
    l = open(os.path.join(os.path.dirname(__file__), '..', 'datasets', 'testNumbers.txt'), 'r').read().splitlines()
    other_points = []
    for line in l:
        fields=line.split(" ")
        other_points.append([int(fields[0]), int(fields[1])])
    l = open(os.path.join(os.path.dirname(__file__), '..', 'datasets', filename), 'r').read().splitlines()
    data_points = []
    for line in l:
        fields=line.split(" ")
        data_points.append([int(fields[0]), int(fields[1])])


    shortest_pos = []
    for i in data_points:
        smallest = 10000000000
        for j in other_points:
            temp = math.sqrt(((i[0] - j[0])**2 + (i[1] - j[1])**2))
            if smallest>temp:
                smallest = temp
                current_points = j
        shortest_pos.append(current_points)
    

    f = open("out_"+filename+".txt", 'w')
    for i in range(len(data_points)):
        f.write("("+str(data_points[i][0]) + ", " + str(data_points[i][1]) + ") -> ("+str(shortest_pos[i][0]) + ", " + str(shortest_pos[i][1]) + ")\n")
    f.close()

do("numbers1.txt")