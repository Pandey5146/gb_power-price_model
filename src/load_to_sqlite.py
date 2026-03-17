import pandas as pd
import sqlite3
from pathlib import Path

db_path = Path("db/market_data.db")

wind_path = Path("data/neso_wind_full_clean.csv")
demand_path = Path("data/neso_demand_clean.csv")

conn = sqlite3.connect(db_path)

# Load wind
df_wind = pd.read_csv(wind_path)
df_wind.to_sql("wind_forecast", conn, if_exists="replace", index=False)

# Load demand
df_demand = pd.read_csv(demand_path)
df_demand.to_sql("demand", conn, if_exists="replace", index=False)

# Checks
wind_count = pd.read_sql("SELECT COUNT(*) AS row_count FROM wind_forecast", conn)
demand_count = pd.read_sql("SELECT COUNT(*) AS row_count FROM demand", conn)

print("Wind table:")
print(wind_count)

print("\nDemand table:")
print(demand_count)

conn.close()
print("\nWind and demand loaded into SQLite successfully.")
