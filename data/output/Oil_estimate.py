import pandas as pd

# Load the saved estimate from CSV
csv_file_path = r'C:\Users\oleva\PycharmProjects\PetroCast\data\processed\Oil_estimate.csv'
saved_data = pd.read_csv(csv_file_path)

saved_output = saved_data['value'].iloc[0]
print(f"Loaded saved output from CSV: {saved_output} ({saved_data['unit'].iloc[0]})")
