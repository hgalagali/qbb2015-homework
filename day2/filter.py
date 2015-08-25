#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
f=open(filename)

#Iterates the file by line number
for line_count, line in enumerate(f):
    if line_count <= 10:
        pass
    elif line_count<=15:
        print line,
    else:
        break
   