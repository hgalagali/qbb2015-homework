#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

#Set counter variable to 0
count=0

#Iterates file by line number and count
for line in f:
    #Look for reads that map to exactly one location in the genome
    if "NH:i:1" in line:
        #Increment counter variable 
        count += 1
    
print "Number of alignments that map to exactly one location on the genome is %s" %count