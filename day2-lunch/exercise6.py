#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

count=0
mapq_total=0
#Iterates file by line number 
for line in f:
    fields=line.split()
    #Removing header lines
    if "@" not in fields[0]:
       mapq_total=mapq_total+int(fields[4])
       count+=1
    
print "Average MAPQ score=%s" %(mapq_total/count)

        