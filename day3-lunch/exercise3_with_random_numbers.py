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
x=mean + std_dev*numpy.random.randn(1000)
x.sort()


plt.figure()
plt.hist(list(df3))
y = mlab.normpdf(x, mean, std_dev)

plt.plot(x, len(df3)*y, 'r--')
plt.xlabel("log FPKM")
plt.ylabel("frequency")
plt.savefig("DensityPlot_with_random_numbers.png")
