import requests
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

url = "https://data.elexon.co.uk/bmrs/api/v1/balancing/pricing/market-index"

params = {
    "from": "2026-03-16T00:00:00Z",
    "to": "2026-03-24T00:00:00Z"
}

response = requests.get(url, params=params, timeout=60)
response.raise_for_status()

data = response.json()

if isinstance(data, dict) and "data" in data:
    records = data["data"]
else:
    records = data

df = pd.DataFrame(records)

file_path = raw_folder / "recent_price.csv"
df.to_csv(file_path, index=False)

print("Downloaded rows:", len(df))
print("Saved to:", file_path)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())
