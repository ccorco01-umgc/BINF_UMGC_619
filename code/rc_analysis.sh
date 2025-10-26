#!/bin/bash
cd ~/BINF_UMGC_619

mkdir -p read_cleaning/results

echo "Extracting pre-QC metrics"
grep -E "SRR27129218|SRR27129336|SRR27129337" multiqc/multiqc_general_stats.txt > read_cleaning/results/pre_qc_summary.txt
sed -i '1iSample\tPercent_Duplicates\tPercent_GC\tAvg_Length\tPercent_Fails\tTotal_Reads' read_cleaning/results/pre_qc_summary.txt

echo "Extracting post-QC metrics"
echo -e "Sample\tTotal_Reads_After\tRead1_Length\tGC_Content(%)" > read_cleaning/results/post_qc_summary.txt

for file in read_cleaning/results/*.fastp.json
do
  sample=$(basename "$file" .fastp.json)
  total=$(grep -m1 '"total_reads"' "$file" | awk -F ':' '{print $2}' | tr -d ', ')
  length=$(grep -m1 '"read1_mean_length"' "$file" | awk -F ':' '{print $2}' | tr -d ', ')
  gc=$(grep -m1 '"gc_content"' "$file" | awk -F ':' '{print $2}' | tr -d ', ')
  gc_percent=$(awk -v val="$gc" 'BEGIN {printf "%.2f", val*100}')
  echo -e "${sample}\t${total}\t${length}\t${gc_percent}" >> read_cleaning/results/post_qc_summary.txt
done

echo "Combining summaries"
paste read_cleaning/results/pre_qc_summary.txt read_cleaning/results/post_qc_summary.txt > read_cleaning/results/qc_comparison_table.txt

echo "Calculating retention"
awk 'NR>1 {pct=($8/$6)*100; print $1, $6, $8, pct}' read_cleaning/results/qc_comparison_table.txt > read_cleaning/results/qc_percent_retained.txt
sed -i '1iSample\tPre_Reads\tPost_Reads\tPercent_Retained' read_cleaning/results/qc_percent_retained.txt

echo "QC comparison completed"

