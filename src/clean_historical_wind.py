import pandas as pd
from pathlib import Path

input_file = Path("data/raw/historical_wind_fuelhh.csv")
output_file = Path("data/historical_wind_clean.csv")

df = pd.read_csv(input_file)

# Keep only WIND rows
df_wind = df[df["fuelType"] == "WIND"].copy()

# Keep only needed columns
df_wind = df_wind[["startTime", "settlementPeriod", "generation"]].copy()

# Rename columns
df_wind = df_wind.rename(columns={
    "startTime": "Datetime",
    "settlementPeriod": "Settlement_Period",
    "generation": "Wind_Actual"
})

# Convert types
df_wind["Datetime"] = pd.to_datetime(df_wind["Datetime"])
df_wind["Wind_Actual"] = pd.to_numeric(df_wind["Wind_Actual"], errors="coerce")

# Drop missing values
df_wind = df_wind.dropna()

# Sort
df_wind = df_wind.sort_values("Datetime").reset_index(drop=True)

# Save
df_wind.to_csv(output_file, index=False)

print("Rows:", len(df_wind))
print("Columns:", df_wind.columns.tolist())
print(df_wind.head())
print(f"Saved to: {output_file}")