# Read Cleaning for Staphylococcus aureus (SRR27129218, SRR27129336, SRR27129337)

#!/bin/bash

# Install tools
sudo apt update
sudo apt install -y fastp wget

# Make folders
cd ~/BINF_UMGC_619
mkdir -p read_cleaning
cd read_cleaning
mkdir -p fastq_rawdata cleaned results

# Check for FASTQ files before downloading
echo "Checking for FASTQ files..."
cd fastq_rawdata

if [ -f SRR27129218_1.fastq.gz ] && [ -f SRR27129218_2.fastq.gz ] && \
   [ -f SRR27129336_1.fastq.gz ] && [ -f SRR27129336_2.fastq.gz ] && \
   [ -f SRR27129337_1.fastq.gz ] && [ -f SRR27129337_2.fastq.gz ]; then
    echo "All FASTQ files already present. Skipping download."
else
    echo "Downloading FASTQ files..."
    wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/018/SRR27129218/SRR27129218_1.fastq.gz
    wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/018/SRR27129218/SRR27129218_2.fastq.gz
    wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/036/SRR27129336/SRR27129336_1.fastq.gz
    wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/036/SRR27129336/SRR27129336_2.fastq.gz
    wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129337/SRR27129337_1.fastq.gz
    wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129337/SRR27129337_2.fastq.gz
fi

cd ..

# Begin read cleaning
echo "Read Cleaning started"

echo "Cleaning SRR27129218"
fastp \
  -i fastq_rawdata/SRR27129218_1.fastq.gz \
  -I fastq_rawdata/SRR27129218_2.fastq.gz \
  -o cleaned/SRR27129218_1.fastp_cleaned.fastq.gz \
  -O cleaned/SRR27129218_2.fastp_cleaned.fastq.gz \
  --detect_adapter_for_pe \
  --qualified_quality_phred 20 \
  --length_required 50 \
  --thread 4 \
  --html results/SRR27129218.fastp.html \
  --json results/SRR27129218.fastp.json

echo "Cleaning SRR27129336"
fastp \
  -i fastq_rawdata/SRR27129336_1.fastq.gz \
  -I fastq_rawdata/SRR27129336_2.fastq.gz \
  -o cleaned/SRR27129336_1.fastp_cleaned.fastq.gz \
  -O cleaned/SRR27129336_2.fastp_cleaned.fastq.gz \
  --detect_adapter_for_pe \
  --qualified_quality_phred 20 \
  --length_required 50 \
  --thread 4 \
  --html results/SRR27129336.fastp.html \
  --json results/SRR27129336.fastp.json

echo "Cleaning SRR27129337"
fastp \
  -i fastq_rawdata/SRR27129337_1.fastq.gz \
  -I fastq_rawdata/SRR27129337_2.fastq.gz \
  -o cleaned/SRR27129337_1.fastp_cleaned.fastq.gz \
  -O cleaned/SRR27129337_2.fastp_cleaned.fastq.gz \
  --detect_adapter_for_pe \
  --qualified_quality_phred 20 \
  --length_required 50 \
  --thread 4 \
  --html results/SRR27129337.fastp.html \
  --json results/SRR27129337.fastp.json

echo "Read cleaning finished successfully."

