#!/usr/bin/env python

import pandas as pd

import matplotlib.pyplot as plt
import numpy
import matplotlib.mlab as mlab 

df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

df2=df[df["FPKM"]>0]

df3=numpy.log(df2["FPKM"])

plt.figure()
pd.Series.plot(df3, 'kde')
plt.xlabel("log FPKM")
plt.ylabel("frequency")
plt.savefig("DensityPlot_modified.png")
