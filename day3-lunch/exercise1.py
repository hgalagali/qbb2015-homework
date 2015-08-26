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
plt.plot(Sxl_f) 
plt.plot(Sxl_m)
plt.savefig("TimeCourse.png")