import pandas as pd
import glob
import os

# Find all quant.sf files in subfolders
files = glob.glob("SRR*/quant.sf")

dfs = []
for f in files:
    sample = os.path.basename(os.path.dirname(f))
    df = pd.read_csv(f, sep="\t")[["Name", "TPM"]]
    df.rename(columns={"TPM": sample}, inplace=True)
    dfs.append(df)

# Merge all samples by gene name
merged = dfs[0]
for df in dfs[1:]:
    merged = merged.merge(df, on="Name", how="outer")

# Calculate average TPM across samples
merged["avg_TPM"] = merged.iloc[:, 1:].mean(axis=1)

# Sort and select top 10
top10 = merged.sort_values("avg_TPM", ascending=False).head(10)

# Save results
os.makedirs("plots", exist_ok=True)
top10.to_csv("plots/top10_genes_table.csv", index=False)

print(" Top 10 genes saved to plots/top10_genes_table.csv")
