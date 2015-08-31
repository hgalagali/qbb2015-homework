#!/usr/bin/env python

"""Prints tuples with sequence name, ratio of identities, ratio of gaps"""

import sys

file = open(sys.argv[1])
output = []

while 1:
    line = file.readline()
    if not line:
        break
    if line.startswith(">"):
        sequence_name=line[1:].strip("\r\n")
    elif line.startswith(" Identities"):
        fields=line.split()
        ratio_of_identities = fields[2]
        ratio_of_gaps = fields[6]
        output.append((sequence_name, ratio_of_identities, ratio_of_gaps))
        
for i in range(0,len(output)):
    print output[i]
        
    
