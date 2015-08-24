#!/bin/bash

echo "This Bash script should echo the commands to run FastQC and HISAT on all 24 samples.  e.g."
echo ""
echo "fastqc /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -o /Users/cmdb/qbb2015/assignments/day1-homework"
echo "hisat -p 4 -x /Users/cmdb/qbb2015/genomes/BDGP6 -U /Users/cmdb/qbb2015/rawdata/SRR072893.fastq.gz -S SRR072893.sam"
echo ""
echo "However, there are 6 mistakes!"

FASTQ_DIR="/Users/cmdb/qbb2015/rawdata"
OUTPUT_DIR="/Users/cmdb/qbb2015/assignments/day1-homework"

GENOME_DIR="/Users/cmdb/qbb2015/genomes"
SAMPLE_PREFIX="SRR072"
ANNOTATION="BDGP6"

CORES=4

for i in {893..916} 
do
  echo "fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -o $OUTPUT_DIR"
  echo "hisat -p 4 -x $GENOME_DIR/$ANNOTATION -U FASTQ_DIR/$SAMPLE_PREFIX$i.fastq.gz -S $SAMPLE_PREFIX$i.sam"
done