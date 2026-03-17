import requests
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

# Historical Initial National Demand outturn stream
url = "https://data.elexon.co.uk/bmrs/api/v1/demand/outturn/stream"

params = {
    "from": "2024-01-01T00:00:00Z",
    "to": "2026-01-01T00:00:00Z",
    "format": "json"
}

response = requests.get(url, params=params, timeout=120)
response.raise_for_status()

data = response.json()

if isinstance(data, dict) and "data" in data:
    records = data["data"]
else:
    records = data

df = pd.DataFrame(records)

file_path = raw_folder / "historical_demand_stream.csv"
df.to_csv(file_path, index=False)

print("Downloaded rows:", len(df))
print("Saved to:", file_path)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())