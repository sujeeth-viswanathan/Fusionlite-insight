import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

ticker = "AAPL"
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

df = yf.download(ticker, start=start_date, end=end_date)

print(f"Downloaded {len(df)} rows of data for {ticker}")
print(df.head())

df.to_csv("data_raw.csv")
