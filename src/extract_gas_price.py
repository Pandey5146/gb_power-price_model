import pandas as pd

url = "https://raw.githubusercontent.com/datasets/oil-prices/master/data/brent-daily.csv"

df = pd.read_csv(url)

df = df.rename(columns={
    "Date": "Datetime",
    "Price": "Gas_Price"
})

df["Datetime"] = pd.to_datetime(df["Datetime"])

df.to_csv("data/gas_price_clean.csv", index=False)

print("Downloaded rows:", len(df))
print(df.head())
print("Saved to data/gas_price_clean.csv")