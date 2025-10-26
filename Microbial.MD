# Group Project: RNA-Seq Workflow (Microbial)

## Preparation
- **GitHub Setup**
  - Team members: __________________________  

## Data Retrieval
- **NCBI SRA accessions used:**
  - SRR27129218_1
  - SRR27129218_2
  - SRR27129336_1
  - SRR27129336_2
  - SRR27129337_1
  - SRR27129337_2

- **Commands used to download data:**
  ```bash
  wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/018/SRR27129218/SRR27129218_2.fastq.gz
  wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/018/SRR27129218/SRR27129218_1.fastq.gz
  wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/036/SRR27129218/SRR27129336_2.fastq.gz
  wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/036/SRR27129218/SRR27129336_1.fastq.gz
  wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129337/SRR27129337_2.fastq.gz
  wget -nc ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR271/037/SRR27129337/SRR27129337_1.fastq.gz

## Quality Control (QC)
- **Tools Used:** 
  - FastQC
  - MultiQC
- **Tasks Performed:**  
  - Generated per-sample QC reports  
  - Summarized read quality, GC content, adapter contamination, duplication  
- **Deliverables:**  
  -Example screenshots included in the `/plots/` directory:  
  - `basic_statistics.png`  
  - `per_base_quality.png`
  - `per_sequence_gc.png`

  -Raw Read Counts and Duplicates
| Sample        | Total Sequences | % Duplicates |
|---------------|-----------------|--------------|
| SRR27129218_1 | 3,858,381       | 62.91%       |
| SRR27129218_2 | 3,858,381       | 63.74%       |
| SRR27129336_1 | 6,012,165       | 52.12%       |
| SRR27129336_2 | 6,012,165       | 52.35%       |
| SRR27129337_1 | 6,723,158       | 49.32%       |
| SRR27129337_2 | 6,723,158       | 50.16%       | 
- **Interpretation:**  
  - Overall, the sequencing data show **good read quality and appropriate GC content**. Adapter contamination was negligible. Duplication levels are elevated but still within a range that allows downstream analysis. With these considerations, the datasets are suitable for further analysis.

## Read Cleaning
- **Tools Used:** 
- **Tasks Performed:**  
- **Deliverables:**  
- **Interpretation:**  

## Alignment
- **Tools Used:** 
  - Salmon
  - Python
  - Matplotlib
  - Pandas
- **Tasks Performed:**  
  - Aligned paired end sequences
  - Created plots to display alignment metrics
- **Deliverables:**  
- Example screenshots included in the `/plots/` directory:  
  - `percent_mapped.png`  
  - `total_reads_processed.png`
- **Interpretation:**  
  - Overall, the alignment was successful. Approximately 3.9M reads were processed for SRR27129218, 6.0M for SRR27129336, 6.7M for SRR27129337. Of the reads that were processed approximately 90%, 87%, and 85% were mapped respectively. A mapping percentage above 80% is considered to be good. 

## Annotation & Quantification
- **Tools Used:** 
- **Tasks Performed:**  
- **Deliverables:**  
- **Interpretation:**  
