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
    count=0
    array_copy=copy.deepcopy(arrays)
    for line in open(fname):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        array_copy[chrom][start:end] = 1
        count+=1
    return count, array_copy 
    
def two_intersection(arrays1, arrays2, fname1, fname2):
    num_overlap=0
    for line in open(fname):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        sl = arrays1[chrom][start:end] & arrays2[chrom][start:end]
        num_overlap += sl.any() 
    return num_overlap 
    
def three_intersection(arrays1, arrays2, arrays3, fname):
    num_overlap=0
    for line in open(fname):
        fields = line.split()
        chrom = fields[0]
        start = int(fields[1])
        end = int(fields[2])
        sl = arrays1[chrom][start:end] & arrays2[chrom][start:end] & arrays3[chrom][start:end]
        num_overlap += sl.any() 
    return num_overlap

arrays = arrays_from_len_file(sys.argv[1])
count_1, arrays1 = set_bits_from_file(arrays, sys.argv[2])
count_2, arrays2 = set_bits_from_file(arrays, sys.argv[3])
count_3, arrays3 = set_bits_from_file(arrays, sys.argv[4])
            
count_1_2 = two_intersection(arrays_1, arrays_2, sys.argv[2])
count_1_3 = two_intersection(arrays_1, arrays_3, sys.argv[2])
count_2_3 = two_intersection(arrays_2, arrays_3, sys.argv[4])
count_1_2_3 = three_intersection(arrays_1, arrays_2, arrays_3, sys.argv[4])

print count_1, count_2, count_3, count_1_2, count_1_3, count_2_3, count_1_2_3
A = count_1 - count_1_2 - count_1_3 + count_1_2_3
B = count_2 - count_1_2 - count_2_3 + count_1_2_3
C = count_3 - count_1_3 - count_2_3 + count_1_2_3
AB = count_1_2 - count_1_2_3
BC = count_2_3 - count_1_2_3
AC = count_1_3 - count_1_2_3

plt.figure()
matplotlib_venn.venn3(subsets = (A,B,AB,C,AC,BC,count_1_2_3), set_labels = (sys.argv[2], sys.argv[3], sys.argv[4]))
plt.savefig("Venn.png")


