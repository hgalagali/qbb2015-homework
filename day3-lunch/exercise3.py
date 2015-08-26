#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy
import matplotlib.mlab as mlab 

df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

df2=df[df["FPKM"]>0]

df3=numpy.log(df2["FPKM"])

    
mean=numpy.mean(df3)
std_dev=numpy.std(df3)


plt.figure()
n, bins, patches = plt.hist(list(df3))
y = mlab.normpdf(bins, mean, std_dev)

plt.plot(bins, len(df3)*y, 'r--')
plt.xlabel("log FPKM")
plt.ylabel("frequency")
plt.savefig("DensityPlot.png")
