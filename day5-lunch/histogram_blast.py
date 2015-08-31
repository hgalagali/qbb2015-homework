#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy

file = open(sys.argv[1])
score = []
e_value =[]
e_value_modified =[]
score_modified =[]

while 1:
    line = file.readline()
    if not line:
        break
    
    else:
        l=line.lstrip()
        if l.startswith("NM"):
            fields=l.split()
            score.append(float(fields[2]))
            e_value.append(float(fields[3]))
            
for i in range(0,len(score)):
    if e_value[i]!=0:
        e_value_modified.append(e_value[i])
        score_modified.append(e_value[i])
        
plt.figure()
plt.title("Alignment scores(bits)")
plt.xlabel("Alignment scores(bits)")
plt.ylabel("Frequency")
plt.hist(numpy.log(score),bins=100)
plt.savefig("Histogram_scores.png")

plt.figure()
plt.title("e-values")
plt.xlabel("e-values")
plt.ylabel("Frequency")
plt.hist(numpy.log(e_value_modified), bins=100)
plt.savefig("Histogram_e_values.png")

plt.figure()
plt.title("e-values vs alignment scores")
plt.ylabel("e-values")
plt.xlabel("alignment score (bits)")
plt.scatter(x=numpy.log(score_modified), y=numpy.log(e_value_modified))
plt.savefig("Scatter.png")



