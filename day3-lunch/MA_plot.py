#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy

df1=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2=pd.read_table("~/qbb2015/stringtie/SRR072900/t_data.ctab")

roi1=df1["FPKM"]>0
roi2=df2["FPKM"]>0

roi=roi1 & roi2

df3=df1[roi]["FPKM"]
df4=df2[roi]["FPKM"]

df5=numpy.log(df3)
df6=numpy.log(df4)

df7=df5-df6
df8=0.5*(df5+df6)

plt.figure()
plt.plot(list(df8), list(df7), 'ro')
plt.title("MA plot")
plt.xlabel("A")
plt.ylabel("M")
plt.savefig("MAplot.png")