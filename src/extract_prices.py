import requests
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

url = "https://data.elexon.co.uk/bmrs/api/v1/datasets/MID"

params = {
    "from": "2026-03-16T00:00:00Z",
    "to": "2026-03-24T00:00:00Z",
    "format": "json"
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

if isinstance(data, dict) and "data" in data:
    records = data["data"]
else:
    records = data

df = pd.DataFrame(records)

output_path = raw_folder / "bmrs_mid_raw.csv"
df.to_csv(output_path, index=False)

print("Downloaded rows:", len(df))
print("Saved to:", output_path)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())
