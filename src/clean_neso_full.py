import pandas as pd
from pathlib import Path

# Paths
input_file = Path("data/raw/neso_wind_full.csv")
output_file = Path("data/neso_wind_full_clean.csv")

# Read raw data
df = pd.read_csv(input_file)

# Keep only useful columns
df_clean = df[["Datetime", "Wind_Forecast", "ForecastDatetime", "Settlement_period", "Capacity"]].copy()

# Convert timestamps
df_clean["Datetime"] = pd.to_datetime(df_clean["Datetime"])
df_clean["ForecastDatetime"] = pd.to_datetime(df_clean["ForecastDatetime"])

# Sort by delivery time
df_clean = df_clean.sort_values("Datetime").reset_index(drop=True)

# Save cleaned file
df_clean.to_csv(output_file, index=False)

print("Cleaned rows:", len(df_clean))
print("Columns:", df_clean.columns.tolist())
print(f"Saved cleaned file to: {output_file}")
print(df_clean.head())
