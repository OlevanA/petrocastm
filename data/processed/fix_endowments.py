import pandas as pd
from pathlib import Path

# Load the CSV file
file_path = "C:/Users/oleva/PycharmProjects/MODPET/data/raw/sorted_oil_endowments_with_estimations.csv"
df = pd.read_csv(file_path)

# Rename columns to match expected format
df_renamed = df.rename(columns={"Estimations": "estimate", "EJ": "value"})

# Keep only the necessary columns
df_fixed = df_renamed[["estimate", "value"]]

# Save the corrected CSV file
df_fixed.to_csv("C:/Users/oleva/PycharmProjects/MODPET/data/processed/Oil_estimate_sorted.csv", index=False)

print("Fixed CSV saved as Oil_estimate.csv")
