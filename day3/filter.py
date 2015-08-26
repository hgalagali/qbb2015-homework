#!/usr/bin/env python

#filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
import sys 
#print sys.argv
#filename=sys.argv[1]

#f=open(filename)

f= sys.stdin

name_counts = {}

#Iterates the file by line number
for line_count, line in enumerate(f):
   fields=line.split()
   gene_name = fields[9]
   if gene_name not in name_counts:
       name_counts[gene_name]=1
   else:
       name_counts[gene_name]+=1
        
for key, value in name_counts.iteritems():
    print key, value
   