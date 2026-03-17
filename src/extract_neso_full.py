import requests
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

url = "https://api.neso.energy/api/3/action/datastore_search"

limit = 1000
offset = 0

all_records = []

while True:

    params = {
        "resource_id": "93c3048e-1dab-4057-a2a9-417540583929",
        "limit": limit,
        "offset": offset
    }

    response = requests.get(url, params=params)
    data = response.json()

    records = data["result"]["records"]

    if not records:
        break

    all_records.extend(records)

    print(f"Downloaded {len(all_records)} rows")

    offset += limit

df = pd.DataFrame(all_records)

print("Total rows:", len(df))

df.to_csv("data/raw/neso_wind_full.csv", index=False)

print("Saved to data/raw/neso_wind_full.csv")
