import pandas as pd

df = pd.read_csv("data_raw.csv", index_col=0)

print(" Missing values per column:")
print(df.isnull().sum())

print("\n Column data types:")
print(df.dtypes)

print("\n Duplicate rows:", df.duplicated().sum())

print("\n Descriptive statistics:")
print(df.describe())

# Clean version
df_clean = df.dropna()
df_clean.to_csv("data_clean.csv")
print("\n Cleaned data saved to 'data_clean.csv'")
