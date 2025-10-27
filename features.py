import pandas as pd

# Load cleaned data
df = pd.read_csv("data_clean.csv", index_col=0)

#Ensure Close is numeric
df["Close"] = pd.to_numeric(df["Close"], errors='coerce')

# Drop rows where close is still null (couldn't convert)
df = df.dropna(subset=["Close"])

# Feature: Daily Return (%)
df["Return"] = df["Close"].pct_change()

# Feature: 5-Day & 10-Day Moving Averages
df["MA5"] = df["Close"].rolling(window=5).mean()
df["MA10"] = df["Close"].rolling(window=10).mean()

# Feature: 5-Day Volatility
df["Volatility5"] = df["Return"].rolling(window=5).std()

# Drop initial NA values (from rolling window)
df.dropna(inplace=True)

# Save features
df.to_csv("features.csv")
print(" Engineered features saved to 'features.csv'")
