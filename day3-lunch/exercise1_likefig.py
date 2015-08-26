#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata=pd.read_csv("~/qbb2015/rawdata/samples.csv")

Sxl_f=[]

for sample in metadata[metadata["sex"]=="female"]["sample"]:
    df=pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxl_f.append(df[roi]["FPKM"].values)
    
Sxl_m=[]

for sample in metadata[metadata["sex"]=="male"]["sample"]:
    df=pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxl_m.append(df[roi]["FPKM"].values)
    
plt.figure()
plt.plot(Sxl_f, 'r', label="female") 
plt.plot(Sxl_m, 'b', label="male")
plt.legend()
plt.ylabel("mRNA abundance (FPKM)")
plt.xlabel("developmental stage")
plt.xticks(range(len(Sxl_f)), ["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation='vertical')
plt.savefig("TimeCourse_likefig.png")