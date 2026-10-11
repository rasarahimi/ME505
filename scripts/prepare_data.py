import pandas as pd
from pathlib import Path

# Load the original dataset
df = pd.read_csv("raw/Fatigue_data.csv")

# Remove the irrelevant identifier
df = df.drop(columns=["Sl. No."])

# Save the processed dataset
Path("processed").mkdir(exist_ok=True)
df.to_csv("processed/Fatigue_processed.csv", index=False)

print("Data preprocessing completed.")
