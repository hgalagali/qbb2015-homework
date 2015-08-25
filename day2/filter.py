#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
f=open(filename)

#Iterates the file by line number
for line in f:
    #Split line on Whitespace
    fields = line.split()
    #Check if column 9 has the string tRNA
    if "tRNA" in fields[9]:
        print line,