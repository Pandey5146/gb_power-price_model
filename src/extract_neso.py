import requests
import pandas as pd
from pathlib import Path

# Create data/raw folder if it doesn't exist
raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)

url = "https://api.neso.energy/api/3/action/datastore_search"
params = {
    "resource_id": "93c3048e-1dab-4057-a2a9-417540583929",
    "limit": 100
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()
records = data["result"]["records"]

df = pd.DataFrame(records)

print("First 5 rows:")
print(df.head())
print("\nColumns:")
print(df.columns.tolist())

output_file = raw_folder / "neso_sample.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved file to: {output_file}")
