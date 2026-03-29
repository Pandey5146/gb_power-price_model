import requests
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta, timezone

raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

url = "https://data.elexon.co.uk/bmrs/api/v1/datasets/FUELHH"

now_utc = datetime.now(timezone.utc)
to_dt = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
from_dt = to_dt - timedelta(days=7)

params = {
    "from": from_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "to": to_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
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
if "startTime" in df.columns:
    s = pd.to_datetime(df["startTime"], errors="coerce")
    print("Min startTime:", s.min())
    print("Max startTime:", s.max())
    print("Unique days:", s.dt.date.nunique())
if "startTime" in df.columns:
    s = pd.to_datetime(df["startTime"], errors="coerce")
    if s.dt.date.nunique() <= 1:
        print("WARNING: Endpoint returned only one day; treat this as latest snapshot, not 7-day history.")
file_path = raw_folder / "historical_wind_fuelhh.csv"
df.to_csv(file_path, index=False)

print("Downloaded rows:", len(df))
print("Saved to:", file_path)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())