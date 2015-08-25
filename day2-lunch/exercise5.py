#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

#Dictionary to keep count
d1={}

#Iterates file by line number and count
for line in f:
    fields=line.split()
    #Removing header lines
    if "@" not in fields[0]: 
        #Counting
        if fields[2] not in d1:
            d1[fields[2]]=1
        else:
            d1[fields[2]]+=1
            
#Printing what is required
for key in ["2L","2R","3L","3R","4","X"]:
    print key, d1[key]
        