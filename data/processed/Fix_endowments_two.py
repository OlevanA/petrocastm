import pandas as pd

# Load URR file
df = pd.read_csv("C:/Users/oleva/PycharmProjects/MODPET/data/processed/Oil_estimate_sorted.csv")

# Print available estimates
print("Available URR keys:", df["estimate"].tolist())
