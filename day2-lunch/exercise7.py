#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/output"
f=open(filename)

count=0
#Iterates file by line number 
for line in f:
    fields=line.split()
    #Removing header lines
    if "@" not in fields[0] and fields[2]=="2L":
       if 10000<=int(fields[3])<=20000:
           count+=1
print count
