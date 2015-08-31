#!/usr/bin/env python

"""Count intersection of 3 BED files and create Venn Diagram"""

import numpy
import sys
import copy
import matplotlib_venn
import matplotlib.pyplot as plt

#create a dictionary that has chromosome name as key and an array of zeros of corresponding size as value 
def arrays_from_len_file(fname):
    arrays = {}
    for line in open(fname):
        fields = line.split()
        name = fields[0]
        size = int(fields[1])
        arrays[name]=numpy.zeros(size, dtype=bool) 
    return arrays

#count # of binding sites for each transcription factor individually
def set_bits_from_file(arrays, fname):
    array_copy=copy.deepcopy(arrays)
    for line in open(fname):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        array_copy[chrom][start:end] = 1
    return array_copy 
    
arrays = arrays_from_len_file(sys.argv[1])
arrays1 = set_bits_from_file(arrays, sys.argv[2])
arrays2 = set_bits_from_file(arrays, sys.argv[3])
arrays3 = set_bits_from_file(arrays, sys.argv[4])

A = 0
B = 0
C = 0
AB = 0
AC = 0
BC = 0
ABC = 0
total = 0

for i in [2,3,4]:
    for line in open(sys.argv[i]):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        check = 0 # to keep track of inclusions
        
        # Check for common regions for all 3
        if (arrays1[chrom][start:end] & arrays2[chrom][start:end] & arrays3[chrom][start:end]).any()==True:
            ABC += 1
            check = 1
            total += 1
        
        # Check for common regions for 2    
        else:
            if (arrays1[chrom][start:end] & arrays2[chrom][start:end]).any()==True:
                AB += 1
                check = 1
                total += 1
           
            if (arrays1[chrom][start:end] & arrays3[chrom][start:end]).any()==True:
                AC += 1
                check = 1
                total += 1
                
            if (arrays2[chrom][start:end] & arrays3[chrom][start:end]).any()==True:
                BC += 1 
                check = 1
                total += 1
        
        # Check for regions for individual        
        if check==0:
            if (arrays1[chrom][start:end]).all()==True:
                A += 1
                total += 1
                
            if (arrays2[chrom][start:end]).all()==True:
                B += 1
                total += 1
                
            if (arrays3[chrom][start:end]).all()==True:
                C += 1
                total += 1
           
            
print A, B, C, AB, AC, BC, ABC, total, A+B+C+AB+AC+BC+ABC

plt.figure()
matplotlib_venn.venn3(subsets = (A,B,AB,C,AC,BC,ABC), set_labels = (sys.argv[2], sys.argv[3], sys.argv[4]))
plt.savefig("Venn_modified.png")


