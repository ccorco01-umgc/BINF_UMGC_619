import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lists of sample names and their corresponding Salmon output files
samples = {
    "SRR27129218": "quant_SRR27129218.sf",
    "SRR27129336": "quant_SRR27129336.sf",
    "SRR27129337": "quant_SRR27129337.sf"
}

dfs = []
# Reads each file, keep gene name and TPM, rename TPM column to sample name
for sample, file in samples.items():
    df = pd.read_csv(file, sep="\t")
    df = df[["Name", "TPM"]]           # keep only gene name and TPM
    df.rename(columns={"TPM": sample}, inplace=True)  # rename TPM to sample name
    dfs.append(df)

# Merges all samples together based on gene names
merged = dfs[0]
for df in dfs[1:]:
    merged = pd.merge(merged, df, on="Name")

# Calculates mean TPM across all samples
merged["Mean_TPM"] = merged[["SRR27129218","SRR27129336","SRR27129337"]].mean(axis=1)

# Gets top 10 most expressed genes
top10 = merged.sort_values("Mean_TPM", ascending=False).head(10)
print(top10)

# Saves top 10 genes to CSV
top10.to_csv("top10_genes_salmon.csv", index=False)

# Makes a heatmap of TPM values for the top 10 genes
plt.figure(figsize=(8,6))
sns.heatmap(top10.set_index("Name")[["SRR27129218","SRR27129336","SRR27129337"]],
            cmap="viridis", annot=True, fmt=".2f")
plt.title("Top 10 Expressed Genes (TPM) - Staphylococcus aureus")
plt.tight_layout()
plt.savefig("top10_heatmap.png", dpi=300)
plt.close()

