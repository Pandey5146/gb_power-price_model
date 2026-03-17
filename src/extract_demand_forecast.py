import requests
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

url = "https://api.neso.energy/api/3/action/datastore_search"

params = {
    "resource_id": "7c0411cd-2714-4bb5-a408-adb065edf34d",
    "limit": 5000
}

response = requests.get(url, params=params, timeout=60)
response.raise_for_status()

data = response.json()
records = data["result"]["records"]

df = pd.DataFrame(records)

file_path = raw_folder / "neso_demand_forecast_raw.csv"
df.to_csv(file_path, index=False)

print("Downloaded rows:", len(df))
print("Saved to:", file_path)
print(df.head())
print("\nColumns:")
print(df.columns.tolist())