import requests
import pandas as pd
from pathlib import Path

url = "https://api.neso.energy/api/3/action/datastore_search"

params = {
    "resource_id": "7c0411cd-2714-4bb5-a408-adb065edf34d",
    "limit": 1000
}

response = requests.get(url, params=params)
data = response.json()

records = data["result"]["records"]

df = pd.DataFrame(records)

output_path = Path("data/raw/neso_demand.csv")
df.to_csv(output_path, index=False)

print("Downloaded rows:", len(df))
print("Saved to:", output_path)
print(df.head())
