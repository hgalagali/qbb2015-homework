#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy 

df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")

df2=df[df["FPKM"]>0]

df3=numpy.log(df2["FPKM"])


plt.figure()
plt.hist(list(df3))
plt.xlabel("log FPKM")
plt.ylabel("frequency")
plt.savefig("Histogram.png")

