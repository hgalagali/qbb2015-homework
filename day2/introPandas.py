#!/usr/bin/env python
import pandas as pd

annotation="/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df=pd.read_table(annotation, comment='#', header=None)

#print df
#print df.head() #prints first 5 rows

#print df.describe() #prints statistics on columns that have integer values
#print df.info() #prints info abt all columns

#print df[1:5] #prints rows 1-4

df.columns = ["chromosome","database","type","start", "end", "score", "strand", "frame", "attributes"] #gives header to columns
#print df.info()

#print df.sort("type", ascending=False) #sorts by type in descending order

#print df["chromosome"] #prints only chromosome number

#print df[["chromosome", "start", "end"]] #prints multiple columns

#print df["start"][9:15] #prints a subarray. order of rows,col does not matter

#print df.shape #prints dimension
#df2=df['start'] 
#print df2.shape

#df2.to_csv("StartColumn.txt", sep='\t', index=False) #saves the start column by removing indices and keeping tab as separator

#roi = df["start"] < 10 #filters df appropriately
#print df[roi] #prints the subtable filtered
#print df[~roi] #prints the rest of the data