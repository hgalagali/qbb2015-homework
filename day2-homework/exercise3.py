#!/usr/bin/env python
import pandas as pd

annotation ="/Users/cmdb/qbb2015/rawdata/samples.csv"

df=pd.read_csv(annotation)

annotation2="/Users/cmdb/qbb2015/stringtie/"

for i in df["sample"]:
    df2=pd.read_table(annotation2+i+"/t_data.ctab")
    roi=df2["t_name"].str.contains("FBtr0331261")
    print df2[roi]
    print "\n"
    