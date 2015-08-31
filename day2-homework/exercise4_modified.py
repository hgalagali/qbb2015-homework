#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")

roi=df["FPKM"]>0
df2=df[roi]

df3=df2["FPKM"]
df4=df3.sort(["FPKM"], inplace=False)

i=df4.count()


top=df4[0:i/3]
middle=df4[i/3:2*(i/3)]
bottom=df4[2*(i/3):i]

plt.figure()
plt.title("FPKM values")
plt.boxplot([top, middle, bottom])
plt.savefig("boxplot_modified.png")