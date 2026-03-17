import pandas as pd
from pathlib import Path

input_file = Path("data/raw/recent_price.csv")
output_file = Path("data/recent_price_clean.csv")

df = pd.read_csv(input_file)

# Keep APX market index price
df = df[df["dataProvider"] == "APXMIDP"].copy()

# Keep needed columns
df = df[["startTime", "settlementPeriod", "price"]]

# Rename columns
df = df.rename(columns={
    "startTime": "Datetime",
    "price": "Price"
})

df["Datetime"] = pd.to_datetime(df["Datetime"])

df = df.sort_values("Datetime").reset_index(drop=True)

df.to_csv(output_file, index=False)

print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print(df.head())
print(f"Saved to: {output_file}")