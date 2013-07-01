#!/usr/bin/python
# -*- coding: utf-8 -*-
def populate_table(values, weights, index, capacity, table):
    if table[index][capacity] != -1:
	return table[index][capacity]
    table[index][capacity] = populate_table(values, weights, index-1,capacity,table)
    if capacity >= weights[index - 1]:
	table[index][capacity] = max(table[index][capacity], values[index-1] + populate_table(values, weights, index-1, capacity-weights[index-1], table))
    return table[index][capacity] 

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # initilazing table
    table = []
    for i in range(items+1):
        table.append([-1 for i in range(capacity+1)])

    # populating base values
    table[0] = [0 for i in range(capacity+1)]
    for i in range(capacity + 1):
        table[0][i] = 0

    # prepare the solution in the specified output format
    value = populate_table(values, weights, items, capacity,table)
    taken = []
    cur = capacity
    for i in range(items):
	if table[items-i][cur] == table[items-1-i][cur]:
	    taken.append(0)
        else: 
	    taken.append(1) 
	    cur = cur - weights[items-1-i]
    taken.reverse()
    outputData = str(value) + ' ' + str(1) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

