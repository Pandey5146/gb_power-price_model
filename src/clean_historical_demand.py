import pandas as pd
from pathlib import Path

input_file = Path("data/raw/historical_demand_stream.csv")
output_file = Path("data/historical_demand_clean.csv")

df = pd.read_csv(input_file)

df_clean = df[["startTime", "settlementPeriod", "initialTransmissionSystemDemandOutturn"]].copy()

df_clean = df_clean.rename(columns={
    "startTime": "Datetime",
    "settlementPeriod": "Settlement_Period",
    "initialTransmissionSystemDemandOutturn": "Demand"
})

df_clean["Datetime"] = pd.to_datetime(df_clean["Datetime"])
df_clean["Demand"] = pd.to_numeric(df_clean["Demand"], errors="coerce")

df_clean = df_clean.dropna()
df_clean = df_clean.sort_values("Datetime").reset_index(drop=True)

df_clean.to_csv(output_file, index=False)

print("Rows:", len(df_clean))
print("Columns:", df_clean.columns.tolist())
print(df_clean.head())
print(f"Saved to: {output_file}")