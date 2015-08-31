#!/usr/bin/env python

import chrombits_modified
import sys
import matplotlib.pyplot as plt
import matplotlib_venn

arr = chrombits_modified.ChromosomeLocationBitArrays(fname=sys.argv[1])

A=arr.copy()
B=arr.copy()
C=arr.copy()

A.set_bits_from_file(fname=sys.argv[2])
B.set_bits_from_file(fname=sys.argv[3])
C.set_bits_from_file(fname=sys.argv[4])
D = A.union(B.union(C))

tuple_list = D.make_tuples()

#print tuple_list

Abc = 0
aBc = 0
abC = 0
ABc = 0
AbC = 0
aBC = 0
ABC = 0
total = 0

for i in tuple_list:
    chrom = i[0]
    start = int(i[1])
    end = int(i[2])
    check = 0 # to keep track of inclusions
        
    # Check for common regions for all 3
    if (A.arrays[chrom][start:end] & B.arrays[chrom][start:end] & C.arrays[chrom][start:end]).any()==True:
        ABC += 1
        check = 1
        total += 1
        
    # Check for common regions for 2    
    else:
        if (A.arrays[chrom][start:end] & B.arrays[chrom][start:end]).any()==True:
            ABc += 1
            check = 1
            total += 1
           
        if (A.arrays[chrom][start:end] & C.arrays[chrom][start:end]).any()==True:
            AbC += 1
            check = 1
            total += 1
                
        if (B.arrays[chrom][start:end] & C.arrays[chrom][start:end]).any()==True:
            aBC += 1 
            check = 1
            total += 1
        
    # Check for regions for individual        
    if check==0:
        if (A.arrays[chrom][start:end]).all()==True:
            Abc += 1
            total += 1
                
        if (B.arrays[chrom][start:end]).all()==True:
            aBc += 1
            total += 1
                
        if (C.arrays[chrom][start:end]).all()==True:
            abC += 1
            total += 1
           
            
print Abc, aBc, abC, ABc, AbC, aBC, ABC, total, Abc+aBc+abC+ABc+AbC+aBC+ABC

plt.figure()
matplotlib_venn.venn3(subsets = (Abc,aBc,ABc,abC,AbC,aBC,ABC), set_labels = (sys.argv[2], sys.argv[3], sys.argv[4]))
plt.savefig("Venn_union.png")
