#Install tools
sudo apt install fastqc
sudo apt install multiqc

#Create output folders
mkdir fastqc
mkdir multiqc

#Get FASTQ
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/018/SRR27129218/SRR27129218_2.fastq.gz
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/018/SRR27129218/SRR27129218_1.fastq.gz
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/036/SRR27129218/SRR27129336_2.fastq.gz
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129218/SRR27129336_1.fastq.gz
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129337/SRR27129337_2.fastq.gz
wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129337/SRR27129337_1.fastq.gz

#Run FastQC
fastqc -t 4 -o fastqc SRR27129218_1.fastq
fastqc -t 4 -o fastqc SRR27129218_2.fastq
fastqc -t 4 -o fastqc SRR27129336_1.fastq
fastqc -t 4 -o fastqc SRR27129336_2.fastq
fastqc -t 4 -o fastqc SRR27129337_1.fastq
fastqc -t 4 -o fastqc SRR27129337_2.fastq

#Run MultiQC
multiqc fastqc -o multiqc

#Generate raw read counts and dups
awk -F'\t' 'BEGIN{OFS=","}NR==1{for(i=1;i<=NF;i++){if($i=="sample")s=i;if($i=="total_sequences")t=i;if($i=="percent_duplicates")d=i}print "sample,total_sequences,percent_duplicates";next}!/^#/&&NF{print $s,$t,$d}' multiqc/multiqc_data/multiqc_fastqc.txt > multiqc/qc_counts_dup.csv



