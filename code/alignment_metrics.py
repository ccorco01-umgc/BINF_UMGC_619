import pandas as pd
import json
import requests
import matplotlib.pyplot as plt
import seaborn as sns

meta_files = {
    "SRR27129218": "https://raw.githubusercontent.com/ccorco01-umgc/BINF_UMGC_619/refs/heads/main/SRR27129218/aux_info/meta_info.json",
    "SRR27129336": "https://raw.githubusercontent.com/ccorco01-umgc/BINF_UMGC_619/refs/heads/main/SRR27129336/aux_info/meta_info.json",
    "SRR27129337": "https://raw.githubusercontent.com/ccorco01-umgc/BINF_UMGC_619/refs/heads/main/SRR27129337/aux_info/meta_info.json"
}

data = []

for sample_name, url in meta_files.items():
    response = requests.get(url)
    if response.status_code == 200:
        meta = response.json()
        data.append({
            "Sample": sample_name,
            "Num Processed": meta.get("num_processed", 0),
            "Percent Mapped": meta.get("percent_mapped", 0.0)
        })
    else:
        print(f"Failed to fetch {url}")

df = pd.DataFrame(data)
sns.set(style="whitegrid")


# Plot 1: Total Reads Processed
plt.figure(figsize=(8, 5))
sns.barplot(x="Sample", y="Num Processed", data=df, palette="Blues_d")
plt.title("Total Reads Processed per Sample")
plt.ylabel("Reads Processed")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("total_reads_processed.png") 
plt.show()

# Plot 2: Percent Mapped
plt.figure(figsize=(8, 5))
sns.barplot(x="Sample", y="Percent Mapped", data=df, palette="Greens_d")
plt.title("Percent Mapped Reads per Sample")
plt.ylabel("Percent Mapped (%)")
plt.ylim(0, 100)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("percent_mapped.png") 
plt.show()

# Save in table format as well
df.to_csv("metrics_table.csv", index=False)