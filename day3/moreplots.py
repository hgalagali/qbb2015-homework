#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata=pd.read_csv("~/qbb2015/rawdata/samples.csv")
Sxl=[]
for sample in metadata[metadata["sex"]=="female"]["sample"]:
    df=pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxl.append(df[roi]["FPKM"].values)
    
plt.figure()
plt.plot(Sxl)
plt.savefig("TimeCourse.png")

df=pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")
df2=pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

plt.figure()
plt.scatter(df["FPKM"], df2["FPKM"])
plt.xlabel("893-male 10")
plt.ylabel("915-female 14")
plt.savefig("scatterplot.png")

chromosomes = {}

for i, line in df.iterrows():
    #print line["chr"]
    if line["chr"] in ["2L", "2R", "3L", "3R", "X", "Y"]:
        if line["chr"] not in chromosomes:
            chromosomes[line["chr"]] = 1
        else:
            chromosomes[line["chr"]] += 1
        
plt.figure()
plt.bar(range(len(chromosomes)), chromosomes.values())
plt.xticks(range(len(chromosomes)), chromosomes.keys())
plt.savefig("barplot.png")