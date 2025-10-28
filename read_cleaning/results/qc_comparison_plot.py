import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in rc_analysis summary files
pre = pd.read_csv("pre_qc_summary.txt", sep="\t")
post = pd.read_csv("post_qc_summary.txt", sep="\t")

# Clean up names so paired-end reads combine properly
pre["Sample"] = pre["Sample"].str.replace("_1", "").str.replace("_2", "")

# Group by sample to sum both ends’ reads
pre_grouped = pre.groupby("Sample", as_index=False)["Total_Reads"].sum()

# Merge with post-QC data
merged = pd.merge(pre_grouped, post, on="Sample")
merged = merged.rename(columns={
    "Total_Reads": "Raw_Reads",
    "Total_Reads_After": "Cleaned_Reads"
})

# Save combined table
merged.to_csv("qc_summary_table.csv", index=False)

# Create side-by-side bar plot for clarity
x = np.arange(len(merged["Sample"]))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(x - width/2, merged["Raw_Reads"], width, label="Raw Reads")
plt.bar(x + width/2, merged["Cleaned_Reads"], width, label="Cleaned Reads")

plt.xlabel("Sample ID")
plt.ylabel("Read Count")
plt.title("Pre- vs Post-QC Read Counts")
plt.xticks(x, merged["Sample"])
plt.legend()
plt.tight_layout()

# Save the plot
plt.savefig("pre_post_QC_readcount_comparison.png", dpi=300)

print("QC comparison table and plot created successfully.")
