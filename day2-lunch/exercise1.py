#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

#Set counter variable to -1 to account for header line
count=0

#Iterates file by line number and count
for line in f:
    field=line.split()
    if "@" not in field[0]:
        count += 1
    
print "Number of alignments is %s" %count