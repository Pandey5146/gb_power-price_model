import pandas as pd

df = pd.read_csv("data/raw/historical_wind_fuelhh.csv")

print("Unique fuel types:")
print(sorted(df["fuelType"].dropna().unique()))