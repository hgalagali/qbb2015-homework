#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

#Set counter variable to 0
count=0

#Iterates file by line number and count
for line in f:
    if "NM:i:0" in line:
        #Increment counter variable 
        count += 1
    
print "Number of alignments that perfectly match to genome is %s" %count