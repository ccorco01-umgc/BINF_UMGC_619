import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the table
df = pd.read_csv("plots/top10_genes_table.csv")
df.set_index("Name", inplace=True)

# Remove avg_TPM column if present
if "avg_TPM" in df.columns:
    df = df.drop(columns=["avg_TPM"])

plt.figure(figsize=(8, 6))
sns.heatmap(df, cmap="viridis", annot=True)
plt.title("Top 10 Expressed Genes (TPM)")
plt.ylabel("Gene")
plt.xlabel("Sample")
plt.tight_layout()
plt.savefig("plots/top10_heatmap.png", dpi=300)
plt.show()

print(" Heatmap saved as plots/top10_heatmap.png")
