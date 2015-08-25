#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

#Set counter variable to 0 
count=0

#Iterates file by line number and count
for line in f:
    fields=line.split()
    #Look for lines 1 to 10 that are not headers 
    if "@" not in fields[0] and count<10:
        print fields[2]
        #Increment counter variable 
        count += 1
    elif count==10:
        break
    
